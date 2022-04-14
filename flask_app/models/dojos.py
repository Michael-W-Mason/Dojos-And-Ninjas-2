#  This is a template for how to do a basic query of the databse. This exampe shows how to pull and create data.

# Allows us to connect to our database and query it
from flask_app.config.mysqlconnection import connectToMySQL

# Create A Class of our DB table
class Dojo:
    # We pass in our data as a dict
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_rows(cls):
        # MySQL query
        query = "SELECT * FROM dojos;"
        # Results returns a list of dictionaries
        results = connectToMySQL("dojos_ninjas_schema").query_db(query)

        # Takes our results and converts a list of dicts to a list of our User instances 
        all_rows = []
        for row in results:
            all_rows.append(Dojo(row))
        # Returns a list of instances
        return all_rows

    @classmethod
    def insert_row(cls, data):
        # MySQL Query
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL("dojos_ninjas_schema").query_db(query, data)
        # return prints if successful
        return results