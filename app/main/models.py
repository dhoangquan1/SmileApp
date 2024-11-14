from datetime import datetime, timezone
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

postTags = db.Table(
    'postTags',
    db.metadata,
    sqla.Column('post_id', sqla.Integer, sqla.ForeignKey('post.id'), primary_key=True),
    sqla.Column('tag_id', sqla.Integer, sqla.ForeignKey('tag.id'), primary_key=True)
)

class Post(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    title : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(150))
    body: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(1500))
    timestamp : sqlo.Mapped[Optional[datetime]] = sqlo.mapped_column(default = lambda : datetime.now(timezone.utc)) 
    likes : sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer, default = 0)
    happiness_level : sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer, default = 3)
    
    tags: sqlo.WriteOnlyMapped['Tag'] = sqlo.relationship(
        secondary=postTags,
        primaryjoin=(postTags.c.post_id == id),
        back_populates="posts"
    )
    
    def get_tags(self):
        return db.session.scalars(self.tags.select()).all()
    
class Tag(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    name: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(20))
    
    posts: sqlo.WriteOnlyMapped['Post'] = sqlo.relationship(
        secondary=postTags,
        primaryjoin=(postTags.c.tag_id == id),
        back_populates="tags"
    )
    
    def __repr__(self):
        return '<Id {} : {} >'.format(self.id,self.name)
    
class User(UserMixin, db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    username: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), unique=True)
    email: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(120), unique=True)
    password_hash: sqlo.Mapped[Optional[str]] = sqlo.mapped_column(sqla.String(256))

    def __repr__(self):
        return '<Id {} : {} >'.format(self.id,self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)