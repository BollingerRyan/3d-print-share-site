from flask_app.config.mysqlconnection import connectToMySQL

db = '3d_prints_db'

class Project:
    def __init__(self,data):
        self.id = data ['id']
        self.project_name = data ['project_name']
        self.description = data ['description']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.user_id = ['user_id']

    @classmethod
    def create_project(cls, data):
        query = '''
        INSERT INTO projects
        (project_name, description, created_at, updated_at ,users_id)
        VALUES (%(project_name)s, %(description)s, NOW(), NOW(), %(users_id)s)
        '''
        result = connectToMySQL(db).query_db(query, data)
        data['id'] = result
        return result
    
    @classmethod
    def get_project_by_users_id(cls, user_id):
        query = '''SELECT * FROM projects WHERE users_id = %(users_id)s'''
        results = connectToMySQL(db).query_db(query, user_id)
        print(f"results: {results}")
        if results:
            return cls(results[0])
        else:
            return None
