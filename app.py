from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

from config import *

database = SQLAlchemy(app)

from models.orm_models.consumption import Consumption

database.create_all()
database.session.commit()

from resources.registration import RegistrationAPI
from resources.authorization import AuthorizationAPI
from resources.add_consumption import AddConsumption

api.add_resource(RegistrationAPI, '/registration/<login>/<password>/<name>/<last_name>/<email>')
api.add_resource(AuthorizationAPI, '/authorization/<login>/<password>')
api.add_resource(AddConsumption, '/post/add-consumption/<token>')


if __name__ == '__main__':
    app.run()
