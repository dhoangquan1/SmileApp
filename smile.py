from config import Config

from app import create_app, db
from app.main.models import Post, Tag, User
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

app = create_app(Config)

@app.shell_context_processor
def make_shell_context():
    return {'sqla': sqla, 'sqlo': sqlo, 'db': db, 'Post': Post, 'Tag' : Tag, 'User' : User}


def add_tags(*args, **kwargs):
    query = sqla.select(Tag)
    if db.session.scalars(query).first() is None:
        tags = [{'name':'funny'},
          {'name':'inspiring'},
          {'name':'true-story'},
          {'name':'heartwarming'}, 
          {'name':'friendship'}  ]
        for t in tags:
            db.session.add(Tag(name = t['name']))
        db.session.commit()  

@app.before_request
def initDB(*args, **kwargs):
    if app._got_first_request:
        db.create_all()
        add_tags()

if __name__ == "__main__":
    app.run(debug=True)