import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_moment import Moment
from flask_migrate import Migrate

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    moment = Moment(app)
    migrate = Migrate(app, db)
    db.init_app(app)
    db.create_all()

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    designation = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    
    def employees(self):
        return {
            'id': self.id,
            'name': self.name,
            'designation': self.designation
        }
    
    def employeedetails(self):
        return {
            'id': self.id,
            'name': self.name,
            'dob': self.dob,
            'designation': self.designation,
            'address': self.address
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return self.employees()