from flask import Blueprint

bp = Blueprint('api',__name__)

from app.api import users

#. GET /api/users/<id> 
#  GET /api/users
#. PUT /api/users/<id>
#  POST /api/users