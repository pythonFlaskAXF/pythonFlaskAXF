import os

basedir= os.path.abspath(os.path.dirname(__file__))


def get_db_uri():

    return 'sqlite:///'+ os.path.join(basedir,'data.sqlite')


class Config:
    DEBUGE = False

    TESTING = False

    SECRET_KEY = '1234567890'

    SQLALCHEMY_TRACK_MODIFICATION = False


class DevelopConfig(Config):

    DEBUGE = True


    SQLALCHEMY_DATABASE_URI = get_db_uri()


envs = {
    'develop':DevelopConfig,
}