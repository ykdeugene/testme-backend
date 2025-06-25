from flask import Blueprint


def create_mcq_blueprint(mongo):
    mcq = Blueprint("example", __name__)

    @mcq.route("/", methods=["GET"])
    def hello():
        return "Hello from blueprint!"

    return mcq
