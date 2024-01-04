from flask import Flask
from flask_smorest import Api
from hello import bp  # Import your blueprint

app = Flask(__name__)
api = Api(app)

api.register_blueprint(bp)








if __name__ == '__main__':
    app.run(debug=True)
