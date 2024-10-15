'''Main Configuration File'''
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    '''Set Flask configuration variables'''
    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    SITE_URL = environ.get('SITE_URL')

    # Database
    MYSQL_HOST = environ.get('MYSQL_HOST')
    MYSQL_USER = environ.get('MYSQL_USER')
    MYSQL_PASS = environ.get('MYSQL_PASS')
    MYSQL_DB = environ.get('MYSQL_DB')
    SQLALCHEMY_DATABASE_URI = (     
        f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}/{MYSQL_DB}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
