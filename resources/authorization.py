from flask_restful import Resource
from flask import jsonify
from service.authorization_service import AuthorizationService
from service.tokenization_service import TokenizationService


class AuthorizationAPI(Resource):
    def get(self, login, password):
        user = AuthorizationService(login, password).check_login()
        if user != 0:
            answer = TokenizationService(user).encode_auth_token()
            return jsonify({"token": answer})
        else:
            return jsonify("Authorization error")
