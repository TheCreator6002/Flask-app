from app import database


class AuthorizationData(database.Model):
    id = database.Column(database.String(250), primary_key=True)
    login = database.Column(database.String(50), unique=True)
    password = database.Column(database.String(500), nullable=True)

    def __repr__(self):
        return 'User %ds>' % self.__login
