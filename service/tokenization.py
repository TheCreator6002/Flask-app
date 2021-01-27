import jwt
import datetime
from config import SECRET_KEY
from models.user import User
import json


class Tokenization:
    """
    Token generation and verification
    """
    def __init__(self, user: User = None):
        self.__user = user

    def encode_auth_token(self) -> str or int:
        """
        Generate authorization token
        :return: string or int
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': self.__user.user_id
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            return token.decode('UTF-8')

        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token) -> User or str:
        """
        Decodes the auth token
        :param auth_token:
        :return: User or str
        """
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            user_id = payload['sub']
            user = User(user_id)
            return user.user_id
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
