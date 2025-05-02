from .db_connection import predictions_collection
from datetime import datetime

class Prediction:
    @staticmethod
    def save_prediction(prediction_data):
        """
        Save prediction data to MongoDB.
        """
        prediction_data['date'] = datetime.now()
        predictions_collection.insert_one(prediction_data)

    @staticmethod
    def get_all_predictions():
        """
        Retrieve all predictions from MongoDB.
        """
        return list(predictions_collection.find({}))