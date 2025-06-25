from flask import Blueprint, jsonify


def create_mcq_blueprint(mongo):
    mcq_blueprint = Blueprint("example", __name__)

    @mcq_blueprint.route("/", methods=["GET"])
    def get_all_mcq():
        cursor = mongo.db.mcq.find()
        documents = list(cursor)
        return jsonify(documents)

    return mcq_blueprint
