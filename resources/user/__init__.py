from flask_smorest import Blueprint

bp = Blueprint('user', __name__, description='Ops on Posts')

from . import routes