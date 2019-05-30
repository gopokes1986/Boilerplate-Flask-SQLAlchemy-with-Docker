from app import db


class ToDo(db.Model):
    """
    A simple SQLAlchemy class for backbone
    """

    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), default='default')
    description = db.Column(db.String(100), default='')

    def __init__(self, category, description):
        self.category = category
        self.description = description

    def __repr__(self):
        return "<Todo {0} {1}>".format(self.category, self.description)