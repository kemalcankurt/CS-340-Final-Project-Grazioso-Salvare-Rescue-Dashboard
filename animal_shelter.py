from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId
import urllib.parse

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user=None, password=None,
                 host='nv-desktop-services.apporto.com',
                 port=30122, db='AAC', col='animals'):
        try:
            # Use fallback values if none provided
            user = user or 'aacuser'
            password = password or 'SNHU'

            # URL-encode in case of special characters
            user_enc = urllib.parse.quote_plus(user)
            pass_enc = urllib.parse.quote_plus(password)

            mongo_uri = f"mongodb://{user_enc}:{pass_enc}@{host}:{port}/?authSource=admin"
            self.client = MongoClient(mongo_uri)
            self.database = self.client[db]
            self.collection = self.database[col]
        except PyMongoError as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise

    def create(self, data):
        """
        Inserts a document into the MongoDB collection.
        :param data: dict - key-value pairs representing the document
        :return: True if insert is successful, else False
        """
        if data:
            try:
                result = self.collection.insert_one(data)
                return True if result.inserted_id else False
            except PyMongoError as e:
                print(f"Insertion failed: {e}")
                return False
        else:
            raise ValueError("Cannot insert empty data")

    def read(self, query):
        """
        Queries documents matching the key/value pair in MongoDB.
        :param query: dict - key-value pair to search
        :return: list of matching documents, or empty list
        """
        try:
            result_cursor = self.collection.find(query)
            results = list(result_cursor)
            return results
        except PyMongoError as e:
            print(f"Read failed: {e}")
            return []
    
    def update(self, query, new_values):
        """
        Updates document(s) in the MongoDB collection that match the query.
        :param query: dict - key-value pair to match documents
        :param new_values: dict - key-value pairs to update
        :return: number of documents modified
        """
        if not query or not new_values:
            raise ValueError("Both query and new_values must be provided")

        try:
            update_result = self.collection.update_many(query, {"$set": new_values})
            return update_result.modified_count
        except PyMongoError as e:
            print(f"Update failed: {e}")
            return 0

    def delete(self, query):
        """
        Deletes document(s) in the MongoDB collection that match the query.
        :param query: dict - key-value pair to match documents
        :return: number of documents deleted
        """
        if not query:
            raise ValueError("Query must be provided")

        try:
            delete_result = self.collection.delete_many(query)
            return delete_result.deleted_count
        except PyMongoError as e:
            print(f"Delete failed: {e}")
            return 0



