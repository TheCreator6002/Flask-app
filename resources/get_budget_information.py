from service.formation_budget_information import FormationBudgetInformation
from service.tokenization_service import TokenizationService
from flask_restful import Resource
from flask import jsonify


class GetBudgetInformation(Resource):
    def get(self, token):
        user = TokenizationService.decode_auth_token(token)
        report = FormationBudgetInformation(user).generate_report()
        token = TokenizationService(user).encode_auth_token()
        return jsonify({"token": token, "report": report})