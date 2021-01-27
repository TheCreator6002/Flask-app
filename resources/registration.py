from flask import jsonify
from flask_restful import Resource
from service.parser import parser
from service.registration_service import RegistrationService
from service.tokenization_service import TokenizationService


class RegistrationAPI(Resource):
    def post(self):
        args = parser.parse_args()
        user = RegistrationService(login=args['login'],
                                   password=args['password'],
                                   name=args['name'],
                                   last_name=args['last name'],
                                   email=args['email']).add_user()
        if user != 0:
            answer = TokenizationService(user).encode_auth_token()
            return jsonify({"token": answer})
        else:
            return jsonify("Registration error")
