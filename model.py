from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Dummy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.message