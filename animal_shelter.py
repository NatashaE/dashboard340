from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    
    def __init__(self, username, password):
        self.client = MongoClient('mongodb://%s:%s@localhost:43664/AAC' % (username, password))
        self.database = self.client['AAC']
        
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True
        else:
            raise Exception("Nothing to save since data parameter is empty.")
            
    def read(self, search_criteria):
        if search_criteria is not None:
            result = self.database.animals.find_one(search_criteria)
            return result
        else:
            raise Exception("Search criteria is empty.")
            
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            result = self.database.animals.update_one(query, new_values)
            return result
        else:
            raise Exception("Either query or values are empty")
            
    def delete(self, query_data):
        if query_data is not None:
            result = self.database.animals.delete_one(query_data)
            return result
        else:
            raise Exception("The query data is empty.")
            