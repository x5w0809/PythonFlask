import os


SESSION_PROTECTION = 'strong'
class Config:
    pjdir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
                 os.path.join(pjdir, 'register.sqlite')
    SECRET_KEY = b'\xa0\x18a\xb0\xb1\x04\xf2B\x182\x0f~\x82d\x8a\x11\xa0\x97\x19\xa1\x8a\x89\x19\x9e'
