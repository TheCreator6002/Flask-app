from models.user import User
from models.orm_models.consumption import Consumption
from models.orm_models.income import Income


class FormationBudgetInformation:
    """
    Generating a report on the user's budget
    """

    def __init__(self, user: User):
        self.__user = user
        self.__consumption_report = {}
        self.__income_report = {}

    def generate_report(self) -> dict:
        report = {'consumption report': FormationBudgetInformation.__get_consumption(self),
                  'income report': FormationBudgetInformation.__get_income(self)}
        return report

    def __get_consumption(self) -> dict:
        """
        Generating a report on user expenses
        :return: dict: Dictionary containing information about expenses
        """
        consumption_data = Consumption.query.filter_by(user_id=self.__user.user_id).all()
        if FormationBudgetInformation.__check_query_result(consumption_data):
            for consumption in consumption_data:
                self.__consumption_report['date'] = consumption.creation_date
                self.__consumption_report['sum'] = consumption.sum
                self.__consumption_report['category'] = consumption.category
            return self.__consumption_report
        else:
            self.__consumption_report['result'] = 'No cost information'
            return self.__consumption_report

    def __get_income(self) -> dict:
        """
        Generating a report on user expenses
        :return: dict: Dictionary containing information about expenses
        """
        income_data = Income.query.filter_by(user_id=self.__user.user_id).all()
        if FormationBudgetInformation.__check_query_result(income_data):
            for income in income_data:
                self.__income_report['date'] = income.creation_date
                self.__income_report['sum'] = income.sum
                self.__income_report['type'] = income.type
            return self.__income_report
        else:
            self.__income_report['result'] = 'No income information'
            return self.__income_report

    @staticmethod
    def __check_query_result(query_result) -> bool:
        """
        Checking for data availability
        :param query_result: response to database query
        :return: bool
        """
        if query_result:
            return True
        else:
            return False

