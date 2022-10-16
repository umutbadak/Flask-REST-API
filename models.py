from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ListingModel(db.Model):
    __table_name__ = 'listings'
    id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.String(200), nullable = False)
    price =  db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f'id: {id}'