class Config:
    MONGO_URI = "mongodb://localhost:27017/mydatabase"
    FRONTEND_URL = "localhost:3000"
    HOST = "localhost"
    PORT = 5000

class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    DEBUG=False