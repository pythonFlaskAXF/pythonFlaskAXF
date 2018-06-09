from flask import Flask
from App.extension import init_extension
from App.settings import envs
from App.views import init_blue


def create_app():

    app = Flask(__name__)

    app.config.from_object(envs.get('develop'))

    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    init_blue(app=app)

    init_extension(app=app)

    return app
