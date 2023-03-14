from flask_app.config.mysqlconnection import connectToMySQL

db = '3d_prints_db'

class Project:
    def __init__(self,data):
        self.id = data ['id']
        self.project_name = data ['project_name']
        self.description = data ['description']
        self.downloads = data ['downloads']
        self.number_of_parts = data ['number_of_parts']
        self.instructions = data ['instructions']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.user_id = ['user_id']