class Config:
    MONGO_URI = "mongodb://root:password@localhost:27017/testme?authSource=admin"
    FRONTEND_URL = "localhost:3000"
    HOST = "127.0.0.1"
    PORT = 5000


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
