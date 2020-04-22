from flask import request, Blueprint, jsonify
from senateBack.models.userModel import User
from senateBack.auth import get_token, validate_token
import uuid
import datetime
import json
import jwt
import os
from pytz import timezone

userBP = Blueprint('userApi', __name__)


@userBP.route('/', methods=['POST'])
def get_my_detail():
    data = request.json
    valid_token, usr_ = validate_token(data)
    if valid_token:
        result = {
            "name": usr_.username,
            "email": usr_.email,
            "varified": usr_.varified,
            "admin":usr_.admin,
            "created_on":usr_.registered_on, 
            "last_update":usr_.last_updated_on
        }

        response_object = {
            'status': 'success',
            'message': 'detail of the user',
            'payload': result
        }
        return jsonify(response_object), 200

    else:
        response_object = {
            'status': 'fail',
            'message': 'invalid token',
        }
        return jsonify(response_object), 300

