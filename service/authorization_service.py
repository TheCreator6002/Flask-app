from werkzeug.security import check_password_hash
from models.orm_models.userprofiles import UserProfiles
from models.orm_models.autorization_data import AuthorizationData
from models.user import User


class AuthorizationService:
    """
    Authorization using the received username and password
    """
    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.__authorization_data = None

    def check_login(self) -> User or int:
        """
        Returns an object User
        In case the user with the passed login does not exist or the wrong password is passed, it will return 0
        :return: User or 0
        """
        if AuthorizationService.__check_authorization_data(self):
            userprofile = UserProfiles.query.filter_by(user_id=self.__authorization_data[0].id).all()
            user = User(user_id=userprofile[0].user_id,
                        name=userprofile[0].name,
                        last_name=userprofile[0].last_name,
                        email=userprofile[0].email,
                        creation_date=userprofile[0].creation_date)
            return user
        else:
            return 0

    def __check_authorization_data(self) -> bool:
        self.__authorization_data = AuthorizationData.query.filter_by(login=self.__login).all()
        password = self.__authorization_data[0].password
        if check_password_hash(password, self.__password):
            return True
        else:
            return False
