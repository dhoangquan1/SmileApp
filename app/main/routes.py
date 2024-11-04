import sys
from flask import render_template, flash, redirect, url_for
import sqlalchemy as sqla

from app import db
from app.main.models import Post
from app.main.forms import PostForm

from app.main import main_blueprint as bp_main

@bp_main.route('/', methods=['GET'])
@bp_main.route('/index', methods=['GET'])
def index():
    posts = db.session.scalars(sqla.select(Post).order_by(Post.timestamp.desc()))
    all_posts  = posts.all()     
    return render_template('index.html', title="Smile Portal", posts=all_posts)

@bp_main.route('/post', methods=['GET', 'POST'])
def postsmile():
    pform = PostForm()
    if pform.validate_on_submit():
        new_post = Post(title = pform.title.data,
                        body = pform.body.data,
                        happiness_level = pform.happiness_level.data,)
        db.session.add(new_post)
        db.session.commit()
        flash('Post "{}" is created!'.format(new_post.title))
        return redirect(url_for('main.index'))
    return render_template('create.html', form = pform)

@bp_main.route('/post/<post_id>/like', methods=['POST'])
def like(post_id):
    thepost = db.session.get(Post, post_id)
    if thepost is None:
        flash('Post with id {} is not found!'.format(post_id))
        return redirect(url_for('main.index'))
    thepost.likes += 1
    db.session.add(thepost)
    db.session.commit()
    return redirect(url_for('main.index'))
    
    
