from flask import Blueprint, request, jsonify, render_template

from flask_bcrypt import Bcrypt
import jwt
import datetime
from models import get_db_connection
from search_engine import fetch_search_results
import os

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

bcrypt = Bcrypt()
SECRET_KEY = os.getenv('SECRET_KEY')

@routes.route('/api/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    password = request.json.get('password')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_password))
    connection.commit()

    return jsonify({'message': 'User created successfully'}), 201

@routes.route('/api/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user and bcrypt.check_password_hash(user['password'], password):
        token = jwt.encode({'user_id': user['id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, SECRET_KEY)
        return jsonify({'token': token, 'user': {'id': user['id'], 'email': user['email']}}), 200
    return jsonify({'error': 'Invalid credentials'}), 401
