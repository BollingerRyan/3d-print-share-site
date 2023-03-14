from flask_app.config.mysqlconnection import connectToMySQL

db = '3d_prints_db'

class Profile:
    def __init__(self,data):
        self.id = data ['id']
        self.Full_name = data ['Full_name']
        self.rank = data ['rank']
        self.description = data ['description']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
