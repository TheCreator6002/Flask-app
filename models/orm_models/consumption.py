from app import database


class Consumption(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    sum = database.Column(database.Integer(150), unique=False)
    category = database.Column(database.String(150), unique=False)
    creation_date = database.Column(database.DateTime)

    user_id = database.Column(database.String(150), database.ForeignKey('user_profiles.user_id'))

    def __repr__(self):
        return str(self.sum) + " " + str(self.category)
