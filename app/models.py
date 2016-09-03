#from app import db,unicode,UserMixin, generate_password_hash, check_password_hash

ROLE_USER = 0
ROLE_ADMIN = 1

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password = db.Column(db.String(255), index = True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def __init__(self, id, username, email, password, role):
        self.id = id
        self.username = username
        self.email = email
        self.set_password(password)
        self.role = role

    def set_password(self, secret):
        self.password = generate_password_hash(secret)

    def check_password(self, secret):
        return check_password_hash(self.password, secret)

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def __repr__(self):
        return 'ID: %r ' % (self.id) + ' USERNAME: %r ' % (self.username) + ' EMAIL: %r ' % (self.email) + ' PASSWORD: %r ' % (self.password) + ' ROLE: %r ' % (self.role)
