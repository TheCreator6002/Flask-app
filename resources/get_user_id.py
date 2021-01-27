from flask_restful import Resource
from flask import jsonify
from service.authorization import Authorization
from service.tokenization import Tokenization


class GetUserId(Resource):
    def get(self, token):
        user = Tokenization.decode_auth_token(token)
        return jsonify(user)
