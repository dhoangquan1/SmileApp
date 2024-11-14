
from flask import render_template, flash, redirect, url_for

from app import db
from app.auth import auth_blueprint as bp_auth 
import sqlalchemy as sqla

from app.auth.auth_forms import RegistrationForm
from app.main.models import User

@bp_auth.route('/user/register', methods=['GET', 'POST'])
def register():
    rform = RegistrationForm()
    if rform.validate_on_submit():
        new_user = User(username = rform.username.data,
                        email = rform.email.data)
        new_user.set_password(rform.password1.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.index'))
    return render_template('register.html', title="Register", form = rform)
