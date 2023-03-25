from flask_app.config.mysqlconnection import connectToMySQL

db = '3d_prints_db'

class Part:
    def __init__(self, data):
        self.id = data['id']
        self.part = data['part']
        self.part_name = data ['part_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.project_id = data['project_id']

    @classmethod
    def create_part(cls, data):
        query = '''
        INSERT INTO parts
        (part, part_name, created_at, updated_at, project_id)
        VALUES (%(part)s, %(part_name)s, NOW(), NOW(), %(project_id)s)
        '''
        result = connectToMySQL(db).query_db(query, data)
        data['id'] = result
        return result

    @classmethod
    def get_parts_by_project_id(cls, project_id):
        query = '''SELECT * FROM parts WHERE project_id = %(project_id)s'''
        results = connectToMySQL(db).query_db(query, project_id)
        parts = []
        for part in results:
            parts.append(cls(part))
        return parts