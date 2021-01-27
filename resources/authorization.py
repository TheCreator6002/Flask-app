from flask_restful import Resource
from flask import jsonify
from service.authorization import Authorization
from service.tokenization import Tokenization


class AuthorizationAPI(Resource):
    def get(self, login, password):
        user = Authorization(login, password).check_login()
        if user != 0:
            answer = Tokenization(user).encode_auth_token()
            return jsonify({"token": answer})
        else:
            return jsonify("Authorization error")
