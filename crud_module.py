from pymongo import MongoClient


class CRUD(object):

    def __init__(self, host, port, database, authentication_database, collection, username, password):
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, host, port))
        self.database = self.client[database]
        self.authentication_database = self.client[authentication_database]
        self.collection = self.database[collection]

    def insert_document(self, data):
        try:
            result = self.collection.insert_one(data)
            if result.inserted_id:
                return True
            else:
                return False
        except Exception as e:
            print("Error inserting document:", str(e))
            return False

    def query_documents(self, query):
        try:
            result = self.collection.find(query)
            return list(result)
        except Exception as e:
            print("Error querying documents:", str(e))
            return[]

    def update_document(self, query, update_data):
        try:
            result = self.collection.update_one(query, {'$set': update_data})
            return result.modified_count
        except Exception as e:
            print("Error updating document:", str(e))
            return 0

    def delete_document(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("Error deleting document:", str(e))
            return 0
