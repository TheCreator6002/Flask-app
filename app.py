from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

from config import *

database = SQLAlchemy(app)

database.create_all()
database.session.commit()

from resources.registration import RegistrationAPI
from resources.authorization import AuthorizationAPI

api.add_resource(RegistrationAPI, '/registration/<login>/<password>/<name>/<last_name>/<email>')
api.add_resource(AuthorizationAPI, '/authorization/<login>/<password>')


if __name__ == '__main__':
    app.run()
