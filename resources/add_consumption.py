from flask_restful import Resource
from service.parser import parser
from service.tokenization_service import TokenizationService
from flask import jsonify


class AddConsumption(Resource):
    def post(self, token):
        args = parser.parse_args()
        user = TokenizationService.decode_auth_token(token)
        user.add_consumption(sum_consumption=int(args['sum']),
                             category=str(args['category']))
        answer = TokenizationService(user).encode_auth_token()
        return jsonify({"token": answer})
