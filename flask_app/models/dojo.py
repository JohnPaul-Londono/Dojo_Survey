from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojos:
    def __init__( self, data ):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]



    @staticmethod
    def validate_ninja(ninja):

        is_valid = True
        if len(ninja["name"]) < 1:
            flash("Name required")
            is_valid = False
        if len(ninja["location"]) < 1:
            flash("Location needed")
            is_valid = False
        if len(ninja["language"]) < 1:
            flash("Language needed")
            is_valid = False
        
        return is_valid
        

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name,location,language,comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);"
        result = connectToMySQL("dojo_survey_schema").query_db(query,data)
        return result

    @classmethod
    def show_ninja(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL("dojo_survey_schema").query_db(query,data)
        return cls(results[0])