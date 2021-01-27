from flask_restful import Resource
from service.registration_service import RegistrationService
from flask import jsonify
from service.tokenization_service import TokenizationService


class RegistrationAPI(Resource):
    def post(self, login, password, name, last_name, email):
        user = RegistrationService(login, password, name, last_name, email).add_user()
        if user != 0:
            answer = TokenizationService(user).encode_auth_token()
            return jsonify({"token": answer})
        else:
            return jsonify("Registration error")
