from flask_app.config.mysqlconnection import connectToMySQL
import base64
from werkzeug.utils import secure_filename

db = '3d_prints_db'

class Profile:
    def __init__(self,data):
        self.id = data ['id']
        self.Full_name = data ['Full_name']
        self.description = data ['description']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.users_id = []


    @classmethod
    def create_profile(cls, data):
        query = '''
        INSERT INTO profile
        (Full_name, Pic, description, users_id, created_at, updated_at)
        VALUES (%(Full_name)s, %(Pic)s, %(description)s, %(users_id)s, NOW(), NOW())
        '''
        return connectToMySQL(db).query_db(query, data)

    
    @classmethod
    def get_users_profile(cls,id):
        query = '''
        SELECT * FROM profile
        WHERE users_id = %(id)s
        '''
        results = connectToMySQL(db).query_db(query, id)
        return results
