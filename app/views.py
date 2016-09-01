from app import (app,
                 request,
                 render_template,
                 url_for,
                 redirect,
                 flash,
                 session,
                 db,
                 g,
                 lm,
                 validators,
                 check_password_hash,
                 generate_password_hash)
from flask_login import (login_user,
                         logout_user,
                         current_user,
                         login_required,
                         unicode,
                         make_next_param,
                         abort)
from .models import (User,
                     ROLE_USER,
                     ROLE_ADMIN)
from .forms import (RegistrationForm,
                    LoginForm)

@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/123')
def onetwothree():
    return render_template('123.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(id=3334, username=form.username.data, email=form.email.data,
                    password=form.password.data,  role=ROLE_USER)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/change', methods=['GET', 'POST'])
def change_password():
    """Password changing."""
    form = PasswordForm()

    if form.validate_on_submit():
        if not current_user.check_password(form.old_password.data):
            form.add_error('old_password', 'Old password is invalid.')
        else:
            with db.transaction:
                current_user.password = form.new_password.data
            return redirect(request.args.get('next') or url_for('settings'))

    return render_template('change_password.html', form=form)

@app.route('/edit', methods=['GET','POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@lm.user_loader
def load_user(id):
    return User.query.get(id)

@app.route('/login', methods=('GET', 'POST'))
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index', title=g.user.username))

    form = LoginForm(request.form)
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user.id'] = user.id
            session['remember_me'] = form.remember_me.data
            login_user(user)
            flash('Welcome %s' % user.username)
            return redirect(url_for('index',  title=g.user.username))
        flash(print(check_password_hash(user.password,user.password)))
        flash('Wrong email or password', 'error-message')

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))