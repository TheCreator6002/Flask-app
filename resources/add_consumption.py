from flask_restful import Resource
from service.parser import parser
from service.tokenization_service import TokenizationService
from flask import jsonify


class AddConsumption(Resource):
    def post(self, token):
        user = TokenizationService.decode_auth_token(token)
        args = parser.parse_args()
        user.add_consumption(sum_consumption=args['sum'],
                             category=args['category'])
        answer = TokenizationService.encode_auth_token(user)
        return jsonify({"token": answer})
