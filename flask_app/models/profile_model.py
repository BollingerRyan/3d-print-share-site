from flask_app.config.mysqlconnection import connectToMySQL



db = '3d_prints_db'

class Profile:
    def __init__(self,data):
        self.id = data ['id']
        self.Full_name = data ['Full_name']
        self.Pic = data['Pic']
        self.description = data ['description']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']


    @classmethod
    def create_profile(cls, data):
        query = '''
        INSERT INTO profile
        (Full_name, Pic, description, users_id, created_at, updated_at)
        VALUES (%(Full_name)s, %(Pic)s, %(description)s, %(users_id)s, NOW(), NOW())
        '''
        return connectToMySQL(db).query_db(query, data)

    
    @classmethod
    def get_users_profile(cls, user_id):
        query = '''
        SELECT * FROM profile
        WHERE users_id = %(user_id)s
        '''
        results = connectToMySQL(db).query_db(query, user_id)
        print(f"results: {results}")
        if results:
            return cls(results[0])
        else:
            return None
        
    @classmethod
    def update_users_profile(cls, user_data):
        query = "UPDATE profile SET Full_name = %(Full_name)s, description = %(description)s, Pic = %(Pic)s, updated_at = NOW() WHERE users_id = %(users_id)s;"
        return connectToMySQL(db).query_db(query, user_data)

