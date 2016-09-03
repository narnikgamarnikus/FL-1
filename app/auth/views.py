from . import (auth,
               render_template,
               flash,
               url_for,
               redirect,
               request,
               session,
               g,
               lm)

from flask_login import (login_user,
                         current_user,
                         login_required,
                         logout_user)
from werkzeug import check_password_hash

from .models import User
from .forms import LoginForm

@auth.before_request
def before_request():
    g.user = current_user

@auth.route('/hello')
def hello():
    return render_template('auth/hello.html')

@auth.route('/')
@auth.route('/index')
def index():
    return render_template('auth/hello.html')

@lm.user_loader
def load_user(id):
    return User.query.get(id)

@auth.route('/login', methods=('GET', 'POST'))
def auth_login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('auth.hello', title=g.user.username))

    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user.id'] = user.id
            session['remember_me'] = form.remember_me.data
            login_user(user)
            flash('Welcome %s' % user.username)
            return redirect(url_for('auth.hello',  title=g.user.username))
        flash(print(check_password_hash(user.password,user.password)))
        flash('Wrong email or password', 'error-message')

    return render_template("auth/login2.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.hello'))