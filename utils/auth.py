from flask import Blueprint
from functools import wraps
from flask import request
from utils.constants import not_authorized_data
import os

auth = Blueprint('auth', __name__)

def authorization(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if not request.headers.get('Authorization') == os.environ.get('API_KEY'):
             return not_authorized_data, 403

        return func(*args, **kwargs)

    return inner

