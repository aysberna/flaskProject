from app import app, api, db
from app.api import bp
from app.models import Users
from config import Config

from flask import request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

@bp.route('/register', methods=['POST'])
def signup_user():  
    data = request.get_json()  

    hashed_password = generate_password_hash(data['password'], method='sha256')
 
    new_user = Users(id=str("123"), username=data['username'], password=hashed_password) 
    db.session.add(new_user)  
    db.session.commit()    

    return jsonify({'message': 'registeration successfully'})

@bp.route('/users', methods=['GET'])
def get_all_users(): 
 
   users = Users.query.all()
   result = []  
   for user in users:  
       user_data = {}
       user_data['username'] = user.username
       user_data['password'] = user.password
     
       result.append(user_data)  
   return jsonify({'users': result})

@bp.route('/login', methods=['POST'])  
def login_user(): 
    auth = request.authorization   
    print('====auth', auth)
    if not auth or not auth.username or not auth.password:  
        return make_response('could not verify', 401, {'Authentication': 'login required"'})    

    user = Users.query.filter_by(name=auth.username).first()   
     
    if check_password_hash(user.password, auth.password):

        token = jwt.encode({'id' : user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, app.config['SECRET_KEY'], "HS256")
        print('=====token', token)
        return jsonify({'token' : token}) 
    
    return make_response('could not verify',  401, {'Authentication': '"login required"'})
