from flask_restful import Resource
from service.parser import parser
from service.tokenization_service import TokenizationService
from flask import jsonify


class AddIncome(Resource):
    def post(self, token):
        args = parser.parse_args()
        user = TokenizationService.decode_auth_token(token)
        user.add_income(sum_income=int(args['sum']),
                        type_income=str(args['type']))
        answer = TokenizationService(user).encode_auth_token()
        return jsonify({"token": answer})
