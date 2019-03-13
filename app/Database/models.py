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
    
    def getPupils():
        all_pupils=Pupil.query.all()
        return all_pupils
    
    def getSpecificPupil(_school_id):
        pupil=Pupil.query.filter_by(school_id=_school_id).first()
        return pupil

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
    math_bot=db.relationship('Math_Bot', lazy=True, backref='mathsbot')
    english_bot=db.relationship('English_Bot', lazy=True, backref='englishbot')
    sst_bot=db.relationship('Sst_Bot', lazy=True, backref='sstbot')
    science_bot=db.relationship('Science_Bot', lazy=True, backref='sciencebot')

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
    __tablename__='mathsbeginning'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    marks=db.Column(db.Integer, nullable=False, default=0)
    aggregate=db.Column(db.Integer, nullable=False, default=9)
    teacher=db.Column(db.String(100), nullable=False)
    Pupil_id=db.Column(db.Integer, db.ForeignKey('pupil.id'))

    def __init__(self, marks, aggregate, teacher, Pupil_id):
        self.marks=marks
        self.aggregate=aggregate
        self.teacher=teacher
        self.Pupil_id=Pupil_id
    
    def mark_subject(_marks, _aggregate, _teacher, _Pupil_id):
        entered_marks=Math_Bot(marks=_marks, aggregate=_aggregate, teacher=_teacher, Pupil_id=_Pupil_id)
        db.session.add(entered_marks)
        db.session.commit()
    
    def edit_subject(_marks, _aggregate):
        updated_marks=Math_Bot(marks=_marks, aggregate=_aggregate)
        db.session.commit()
    
    def __repr__(self):
        math_object={
            "Marks":self.marks,
            "Aggregate":self.aggregate
        }

        return json.dumps(math_object)

class English_Bot(db.Model):
    __tablename__='englishbeginning'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    marks=db.Column(db.Integer, nullable=False, default=0)
    aggregate=db.Column(db.Integer, nullable=False, default=9)
    teacher=db.Column(db.String(100), nullable=False)
    Pupil_id=db.Column(db.Integer, db.ForeignKey('pupil.id'))

    def __init__(self, marks, aggregate, teacher, Pupil_id):
        self.marks=marks
        self.aggregate=aggregate
        self.teacher=teacher
        self.Pupil_id=Pupil_id
    
    def mark_subject(_marks, _aggregate, _teacher, _Pupil_id):
        entered_marks=English_Bot(marks=_marks, aggregate=_aggregate, teacher=_teacher, Pupil_id=_Pupil_id)
        db.session.add(entered_marks)
        db.session.commit()
    
    def edit_subject(_marks, _aggregate):
        updated_marks=English_Bot(marks=_marks, aggregate=_aggregate)
        db.session.commit()
    
    def __repr__(self):
        english_object={
            "Marks":self.marks,
            "Aggregate":self.aggregate
        }

        return json.dumps(english_object)

class Sst_Bot(db.Model):
    __tablename__='sstbeginning'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    marks=db.Column(db.Integer, nullable=False, default=0)
    aggregate=db.Column(db.Integer, nullable=False, default=9)
    teacher=db.Column(db.String(100), nullable=False)
    Pupil_id=db.Column(db.Integer, db.ForeignKey('pupil.id'))

    def __init__(self, marks, aggregate, teacher, Pupil_id):
        self.marks=marks
        self.aggregate=aggregate
        self.teacher=teacher
        self.Pupil_id=Pupil_id
    
    def mark_subject(_marks, _aggregate, _teacher, _Pupil_id):
        entered_marks=Sst_Bot(marks=_marks, aggregate=_aggregate, teacher=_teacher, Pupil_id=_Pupil_id)
        db.session.add(entered_marks)
        db.session.commit()
    
    def edit_subject(_marks, _aggregate):
        updated_marks=Sst_Bot(marks=_marks, aggregate=_aggregate)
        db.session.commit()
    
    def __repr__(self):
        sst_object={
            "Marks":self.marks,
            "Aggregate":self.aggregate
        }

        return json.dumps(sst_object)

class Science_Bot(db.Model):
    __tablename__='sciencebeginning'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    marks=db.Column(db.Integer, nullable=False, default=0)
    aggregate=db.Column(db.Integer, nullable=False, default=9)
    teacher=db.Column(db.String(100), nullable=False)
    Pupil_id=db.Column(db.Integer, db.ForeignKey('pupil.id'))

    def __init__(self, marks, aggregate, teacher, Pupil_id):
        self.marks=marks
        self.aggregate=aggregate
        self.teacher=teacher
        self.Pupil_id=Pupil_id
    
    def mark_subject(_marks, _aggregate, _teacher, _Pupil_id):
        entered_marks=Science_Bot(marks=_marks, aggregate=_aggregate, teacher=_teacher, Pupil_id=_Pupil_id)
        db.session.add(entered_marks)
        db.session.commit()
    
    def edit_subject(_marks, _aggregate):
        updated_marks=Science_Bot(marks=_marks, aggregate=_aggregate)
        db.session.commit()
    
    def __repr__(self):
        science_object={
            "Marks":self.marks,
            "Aggregate":self.aggregate
        }

        return json.dumps(science_object)