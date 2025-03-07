from pymongo import MongoClient

MONGO_URI="mongodb+srv://radhemaaji09:SxLuoTkLj4DoEoOx@lung-cancer-db.k71yk.mongodb.net/lung_cancer_db?retryWrites=true&w=majority&appName=lung-cancer-db"

try:
    client = MongoClient(MONGO_URI)
    db = client["lung_cancer_db"]
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print("❌ Connection failed:", e)
