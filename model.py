from flask_register import db,bcrypt
import bcrypt
from werkzeug.security import check_password_hash,generate_password_hash



class UserRegister(db.Model):
    __tablename__ = 'UserRegisters'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(50), nullable=False)

    @property
    def password(self):
        raise AttributeError('you cant read it')

    @password.setter
    def password(self, password):
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return 'username:%s, email:%s' % (self.username, self.email)


