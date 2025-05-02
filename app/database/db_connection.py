from pymongo import MongoClient
from config.config import Config

# Initialize MongoDB client
client = MongoClient(Config.MONGO_URI)

# Ensure the database name is correctly retrieved from the URI
db = client.get_database('lung-cancer-db')  # Automatically gets the database from MONGO_URI

# Collection for predictions
predictions_collection = db["predictions"]  # Explicitly use dictionary-style access
