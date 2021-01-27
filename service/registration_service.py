from werkzeug.security import generate_password_hash
from app import database
from flask_sqlalchemy import UnmappedClassError
from models.orm_models.user_profiles import UserProfiles
from models.orm_models.autorization_data import AuthorizationData
from models.user import User
from datetime import datetime
import uuid


class RegistrationService:
    """
    Registration of a new user in the system
    """
    def __init__(self, login, password, name, last_name, email):
        self.__login = login
        self.__password = generate_password_hash(password)
        self.__name = name
        self.__last_name = last_name
        self.__email = email
        self.__creation_date = datetime.now()

    def add_user(self) -> User or int:
        """
        Adding a new user record to the database
        If a user with this login already exists, it will return 0
        """
        try:
            user_identity = uuid.uuid4()
            authorization_data = AuthorizationData(id=str(user_identity),
                                                   login=self.__login,
                                                   password=self.__password)
            database.session.add(authorization_data)
            database.session.flush()

            userprofile = UserProfiles(name=self.__name,
                                       last_name=self.__last_name,
                                       email=self.__email,
                                       creation_date=self.__creation_date, user_id=authorization_data.id)
            database.session.add(userprofile)
            database.session.commit()

        except UnmappedClassError:

            database.session.rollback()
            return 0

        user = User(user_id=str(user_identity),
                    name=self.__name,
                    last_name=self.__last_name,
                    email=self.__email,
                    creation_date=self.__creation_date)

        return user


