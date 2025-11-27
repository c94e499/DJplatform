"""Entry point for running the Flask application."""
import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Debug mode is controlled by config, not set directly
    # In production, use gunicorn instead
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug)
