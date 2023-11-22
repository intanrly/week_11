import os

from flask import Flask
from flasktest import app as application

if __name__ == '__main__':
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = os.environ.get('FLASK_PORT', '8001')
    application.run(host=host, port=port)