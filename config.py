import os

basedir = os.path.abspath(os.path.dirname(__file__))
"""
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:default@127.0.0.1:3643/mysql' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
3306
"""
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:default@127.0.0.1:3306/mysql'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


