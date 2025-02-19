from flask import Flask
from flask_cors import CORS
from routes import routes
import os

app = Flask(__name__, 
           static_folder=os.path.join(os.path.dirname(__file__), '../frontend/static'),
           template_folder=os.path.join(os.path.dirname(__file__), '../frontend'))
CORS(app)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
