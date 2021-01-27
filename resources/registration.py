from flask_restful import Resource
from service.registration import Registration
from flask import jsonify
from service.tokenization import Tokenization


class RegistrationAPI(Resource):
    def get(self, login, password, name, last_name, email):
        user = Registration(login, password, name, last_name, email).add_user()
        if user != 0:
            answer = Tokenization(user).encode_auth_token()
            return jsonify({"token": answer})
        else:
            return jsonify("Registration error")