from models.autorization_data import AuthorizationData


class User:
    def __init__(self, user_id: str, name: str = None, last_name: str = None, email: str = None, creation_date=None):
        self.__user_id = user_id
        self.__name = name
        self.__last_name = last_name
        self.__email = email
        self.__creation_date = creation_date

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def user_id(self):
        return self.__user_id


