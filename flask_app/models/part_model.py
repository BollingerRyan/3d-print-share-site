from flask_app.config.mysqlconnection import connectToMySQL

db = '3d_prints_db'

class Part:
    def __init__(self,data):
        self.id = data ['id']
        self.part = data ['part']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.project_id = []