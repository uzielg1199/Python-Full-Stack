from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Band:
    db = 'bands'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.genre = data['genre']
        self.home_city = data['home_city']
        self.founders_id = data['founders_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO bands (name, genre, home_city, founders_id) VALUES (%(name)s,%(genre)s,%(home_city)s,%(founders_id)s);"
        return connectToMySQL('bands').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM bands;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_bands = []
        for row in results:
            all_bands.append( cls(row) )
        return all_bands

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM bands WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE bands SET name=%(name)s, genre=%(genre)s, home_city=%(home_city)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM bands WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_band(band):
        is_valid = True
        if len(band['name']) < 2:
            is_valid = False
            flash("Name must be at least 2 characters","band")
        if len(band['genre']) < 2:
            is_valid = False
            flash("Genre must be at least 2 characters","band")
        if len(band['home_city']) < 2:
            is_valid = False
            flash("Home city must be at least 2 characters","band")
        return is_valid