from models.orm_models.consumption import Consumption
from models.orm_models.income import Income
from flask_sqlalchemy import UnmappedClassError
import datetime
from app import database


class User:
    """
    Service user
    Has the ability to add data on financial transactions to the system
    """
    def __init__(self,
                 user_id: str,
                 name: str = None,
                 last_name: str = None,
                 email: str = None,
                 creation_date=None):
        """
        User initialization can only be performed by identifier
        Filling in all fields is required when you next call the registration service
        :param user_id:
        :param optional name:
        :param optional last_name:
        :param optional email:
        :param optional creation_date:
        """
        self.__user_id = user_id
        self.__name = name
        self.__last_name = last_name
        self.__email = email
        self.__creation_date = creation_date

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name

    def add_consumption(self, sum_consumption: int or float, category: str):
        """
        Adding a new consumption record to the database
        :param sum_consumption:
        :param category:
        """
        User.__consumption_data_check(sum_consumption, category)
        try:
            consumption = Consumption(sum=sum_consumption,
                                      category=category,
                                      creation_date=datetime.datetime.now(),
                                      user_id=self.user_id)

            database.session.add(consumption)
            database.session.commit()

        except UnmappedClassError:

            database.session.rollback()

    def add_income(self, sum_income: int or float, type_income: str):
        """
        Adding a new income record to the database
        :param sum_income:
        :param type_income:
        """
        User.__income_data_check(sum_income, type_income)
        try:
            income = Income(sum=sum_income,
                            type=type_income,
                            creation_date=datetime.datetime.now(),
                            user_id=self.user_id)
            database.session.add(income)
            database.session.commit()

        except UnmappedClassError:

            database.session.rollback()

    @staticmethod
    def __consumption_data_check(sum_consumption, category):
        """
        Data validation before adding
        :param sum_consumption:
        :param category:
        :return: Exception
        """
        if not isinstance(sum_consumption, (int, float)):
            raise TypeError('Expected consumption sum type: int or float')
        if isinstance(category, str):
            raise TypeError('Expected category type: str')

    @staticmethod
    def __income_data_check(sum_income, type_income):
        """
        Data validation before adding
        :param sum_income:
        :param type_income:
        :return: Exception
        """
        if not isinstance(sum_income, (int, float)):
            raise TypeError('Expected income sum type: int or float')
        if not isinstance(type_income, str):
            raise TypeError('Expected income type: str')
