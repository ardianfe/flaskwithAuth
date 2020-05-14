import datetime
from .db import db  
from datetime import date
from flask_bcrypt import generate_password_hash, check_password_hash



class Result(db.Document):
    no_cert = db.StringField()
    co_id = db.ReferenceField('Company')
    title = db.StringField(max_length=60)
    data_gen = db.DictField()
    data_wks = db.DictField()
    category = db.StringField()
    create_time = db.DateTimeField(default=datetime.datetime.now)


class Company(db.Document):
    name_co = db.StringField(required=True)
    address = db.StringField(max_length=200, required=True)
    contact = db.StringField(max_length=60)
    handphone = db.StringField(max_length=60)
    email = db.EmailField()
    create_time = db.DateTimeField(default=datetime.datetime.now)
    lastModified = db.DateTimeField()
    status = db.StringField(max_length=10)
    result = db.ListField(db.ReferenceField('Result', reverse_delete_rule=db.PULL))




class User(db.Document):
    username = db.StringField(required=True, unique=True, min_length=6)
    email = db.EmailField()
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)



    