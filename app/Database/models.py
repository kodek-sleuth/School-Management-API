import json
from app import *

class Admin(db.Model):
    __tablename__="admin"
    
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(100), nullable=False, unique=True)
    username=db.Column(db.String(100), nullable=False, unique=True)
    password=db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, username, password):
        self.name=name
        self.username=username
        self.password=password
    
    def addAdmin(_name, _username, _password):
        admin_to_add=Admin(name=_name, username=_username, password=_password)
        db.session.add(admin_to_add)
        db.session.commit()
    
    def __repr__(self):
        admin_object={
            "Id":self.id,
            "Username":self.username,
            "Name":self.name
        }

        return json.dumps(admin_object)

class Pupil(db.Model):
    __tablename__="pupil"

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(100), nullable=False, unique=True)
    date_of_birth=db.Column(db.String(100), nullable=False)
    age=db.Column(db.Integer, nullable=False)
    class_stream=db.Column(db.String(100), nullable=False)
    guardian=db.Column(db.String(200), nullable=False)
    phone_number=db.Column(db.String(100), nullable=False)
    school_id=db.Column(db.String(100), nullable=False)

    def __init__(self, name, date_of_birth, age, class_stream, guardian, phone_number, school_id):
        self.name=name
        self.date_of_birth=date_of_birth
        self.age=age
        self.class_stream=class_stream
        self.guardian=guardian
        self.phone_number=phone_number
        self.school_id=school_id
    
    def addPupil(_name, _date_of_birth, _age, _class_stream, _guardian, _phone_number, _school_id):
        newPupil=Pupil(name=_name, date_of_birth=_date_of_birth, age=_age, class_stream=_class_stream, guardian=_guardian, phone_number=_phone_number, school_id=_school_id)
        db.session.add(newPupil)
        db.session.commit()
    
    def __repr__(self):
        pupil_object={
            "Name":self.name,
            "Class":self.class_stream,
            "School_id":self.school_id
        }

        return json.dumps(pupil_object)

class Math_Bot(db.Model):
    pass




