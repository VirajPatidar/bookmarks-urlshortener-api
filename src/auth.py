from os import access
from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from flask import Blueprint, app, request, jsonify

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.post('/register')
def register():
    return jsonify({
        'message': "User created",
    }), HTTP_201_CREATED


@auth.get("/me")
def me():
    return jsonify({
        'username': 'user.username',
        'email': 'user.email'
    }), HTTP_200_OK
