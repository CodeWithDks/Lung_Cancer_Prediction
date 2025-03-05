import os
import joblib
import logging
from flask import Blueprint, render_template, request, jsonify, current_app
from .utils.prediction_helper import prepare_input_data
from config.config import Config

# Create blueprint
main_blueprint = Blueprint('main', __name__)

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_model():
    """
    Load the machine learning model with improved error handling
    """
    try:
        model_path = current_app.config.get('MODEL_PATH', Config.MODEL_PATH)
        
        if not os.path.exists(model_path):
            logger.error(f"Model file not found at {model_path}")
            return None
        
        model = joblib.load(model_path)
        logger.info("Model loaded successfully")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        return None

@main_blueprint.route('/')
def index():
    """
    Render the main index page
    """
    return render_template('index.html')

@main_blueprint.route('/predict', methods=['POST'])
def predict():
    """
    Handle prediction requests with comprehensive error handling
    """
    try:
        # Validate input data
        if not request.is_json:
            return jsonify({
                'error': 'Invalid input. JSON required.',
                'status': 'input_error'
            }), 400

        # Get input data
        input_data = request.json
        
        # Validate all required features are present
        feature_names = current_app.config.get('FEATURE_NAMES', Config.FEATURE_NAMES)
        missing_features = [f for f in feature_names if f not in input_data]
        
        if missing_features:
            return jsonify({
                'error': f'Missing required features: {", ".join(missing_features)}',
                'status': 'input_error'
            }), 400

        # Load the model
        model = load_model()
        
        # Check if model is loaded
        if model is None:
            return jsonify({
                'error': 'Machine learning model could not be loaded',
                'status': 'error'
            }), 500
        
        # Prepare input data
        input_df = prepare_input_data(input_data, feature_names)
        
        # Make prediction
        prediction = model.predict(input_df)
        
        # Get class labels
        class_labels = current_app.config.get('CLASS_LABELS', Config.CLASS_LABELS)
        predicted_label = class_labels[prediction[0]]
        
        # Log prediction
        logger.info(f"Prediction made: {predicted_label}")
        
        # Return prediction
        return jsonify({
            'prediction': predicted_label,
            'status': 'success'
        })
    
    except ValueError as ve:
        # Handle input validation errors
        logger.warning(f"Input validation error: {str(ve)}")
        return jsonify({
            'error': str(ve),
            'status': 'input_error'
        }), 400
    
    except Exception as e:
        # Handle unexpected errors
        logger.error(f"Unexpected prediction error: {str(e)}")
        return jsonify({
            'error': 'An unexpected error occurred during prediction',
            'status': 'error'
        }), 500
