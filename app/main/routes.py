import sys
from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
import sqlalchemy as sqla

from app import db
from app.main.models import Post, Tag, postTags
from app.main.forms import PostForm, SortForm

from app.main import main_blueprint as bp_main

@bp_main.route('/', methods=['GET'])
@bp_main.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    sform = SortForm()
    query = sqla.select(Post).order_by(Post.timestamp.desc())

    if sform.validate_on_submit():
        if sform.choice.data == 'Date':
            query = sqla.select(Post).order_by(Post.timestamp.desc())
        elif sform.choice.data == 'Title':
            query = sqla.select(Post).order_by(Post.title)
        elif sform.choice.data == '# of likes':
            query = sqla.select(Post).order_by(Post.likes.desc())
        elif sform.choice.data == 'Happiness level':
            query = sqla.select(Post).order_by(Post.happiness_level.desc())
    
    all_posts  = db.session.scalars(query).all()
    postCount = db.session.query(Post).count() 
        
    return render_template('index.html', title="Smile Portal", posts=all_posts, postCount=postCount, sform=sform)
    

@bp_main.route('/post', methods=['GET', 'POST'])
@login_required
def postsmile():
    pform = PostForm()
    if pform.validate_on_submit():
        new_post = Post(title = pform.title.data,
                        body = pform.body.data,
                        happiness_level = pform.happiness_level.data,
                        user_id = current_user.id)
        db.session.add(new_post)
        for t in pform.tag.data:
            new_post.tags.add(t)
        db.session.commit()
        flash('Post "{}" is created!'.format(new_post.title))
        return redirect(url_for('main.index'))
    return render_template('create.html', form = pform)

@bp_main.route('/post/<post_id>/like', methods=['POST'])
@login_required
def like(post_id):
    thepost = db.session.get(Post, post_id)
    if thepost is None:
        flash('Post with id {} is not found!'.format(post_id))
        return redirect(url_for('main.index'))
    thepost.likes += 1
    db.session.add(thepost)
    db.session.commit()
    return redirect(url_for('main.index'))
    
    
