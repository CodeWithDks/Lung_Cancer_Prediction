from flask import Flask

def create_app(config_name='development'):
    # Create Flask app instance
    app = Flask(__name__)
    
    # Configure the app
    if config_name == 'production':
        from config.config import ProductionConfig
        app.config.from_object(ProductionConfig)
    else:
        from config.config import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)
    
    # Import and register blueprints
    from .main import main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app