from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50)) #names cannot be more than 50 characters
    species = db.Column(db.String)
