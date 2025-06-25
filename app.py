# external imports
from flask import Flask
from flask_pymongo import PyMongo
from pymongo.errors import ConnectionFailure
from flask_cors import CORS

# internal imports
from config import DevConfig
from routes.mcq import create_mcq_blueprint

# initialize Flask and config
app = Flask(__name__)
app.config.from_object(DevConfig)
CORS(app)
# CORS(app, origins=[app.config["FRONTEND_URL"]])

# initialize mongo
mongo = PyMongo(app)

try:
    mongo.db.command("ping")
    print("MongoDB connection successful!")
except ConnectionFailure:
    print("MongoDB connection failed!")
    exit(1)

# define and register blueprints
mcq_blueprint = create_mcq_blueprint(mongo)
app.register_blueprint(mcq_blueprint, url_prefix="/mcq")

if __name__ == "__main__":
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config.get("DEBUG", False),
    )
