from app import database


class UserProfiles(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(150), unique=False)
    last_name = database.Column(database.String(150), unique=False)
    email = database.Column(database.String(150), unique=False)
    creation_date = database.Column(database.DateTime)

    user_id = database.Column(database.String(150), database.ForeignKey('authorization_data.id'))

    def __repr__(self):
        return str(self.name) + " " + str(self.last_name)
