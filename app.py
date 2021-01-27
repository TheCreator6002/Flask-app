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
from resources.add_consumption import AddConsumption
from resources.add_income import AddIncome
from resources.get_budget_information import GetBudgetInformation

api.add_resource(RegistrationAPI, '/registration')
api.add_resource(AuthorizationAPI, '/authorization/<login>/<password>')
api.add_resource(AddConsumption, '/post/add-consumption/<token>')
api.add_resource(AddIncome, '/post/add-income/<token>')
api.add_resource(GetBudgetInformation, '/get/get-budget-information/<token>')


if __name__ == '__main__':
    app.run()
