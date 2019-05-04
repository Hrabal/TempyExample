import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'very secret string!'

db_name = basedir.split('/')[-1] + '.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, db_name)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SQLALCHEMY_TRACK_MODIFICATIONS = False
