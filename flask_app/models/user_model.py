import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")

db = '3d_prints_db'

class User:
    def __init__(self, data):
        self.id = data ['id']
        self.username = data ['username']
        self.password = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.profile = []

    @classmethod
    def Reg_user(cls,data):
        query = '''
        INSERT INTO users
        ( first_name, last_name, password,
        email, created_at, updated_at )
        VALUES ( %(first_name)s, %(last_name)s,
        %(email)s, %(password)s,  NOW(), NOW() );
        '''
        return connectToMySQL(db).query_db( query, data )
    

    @staticmethod
    def validations(data):
        is_valid = True
        query = '''
        SELECT * FROM users
        WHERE email = %(email)s
        '''
        results = connectToMySQL(db).query_db( query, data)
        if len(data['password']) < 2:
            flash('Password must have a minimum of 8 characters, use a at least one number one letter and one specaial character')
            is_valid = False
        if len(data['first_name']) < 2:
            flash("first name must be at least 2 characters","register")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters","register")
            is_valid = False
        if len(results) >= 1:
            flash("Email already taken","register")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("email must be in valid format","register")
            is_valid = False
        if not PASS_REGEX.match(data['password']):
            flash("Password must have a minimum of 8 characters, use a at least one number one letter and one specaial character","register")
            is_valid = False
        if data['password'] != data['confirmpassword']:
            flash("passwords do not match","register")
            is_valid = False
        return is_valid