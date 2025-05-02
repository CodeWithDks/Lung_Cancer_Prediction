import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    MODEL_PATH = 'app/ml_model/lung_cancer_model.pkl'
    
    FEATURE_NAMES = [
        'GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY', 'PEER_PRESSURE',
        'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING', 'ALCOHOL CONSUMING',
        'COUGHING', 'SHORTNESS OF BREATH', 'SWALLOWING DIFFICULTY', 'CHEST PAIN'
    ]
    
    
    CLASS_LABELS = {0: "No Cancer", 1: "Lung Cancer"}

    # MongoDB Configuration
    MONGO_URI = os.environ.get('MONGO_URI')
    
    if not MONGO_URI:
        raise ValueError("❌ MONGO_URI is not set in .env file!")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
