# external imports
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from marshmallow import ValidationError
from bson import ObjectId
from bson.errors import InvalidId

# internal imports
from models.topic_schema import TopicSchema


def create_mcq_blueprint(mongo):
    mcq_blueprint = Blueprint("example", __name__)

    @mcq_blueprint.route("/all-topics", methods=["GET"])
    def get_all_topics():
        print("get all topics..")
        cursor = mongo.db.mcq.find({}, {"topic": 1})
        documents = list(cursor)
        print(documents)
        return jsonify(documents)

    @mcq_blueprint.route("/topic-by-id", methods=["GET"])
    def get_topic_by_id():
        print("get topic by id..")
        topic_id = request.args.get("id")
        if not topic_id:
            return jsonify({"error": "Missing 'id' query parameter"}), 400

        try:
            obj_id = ObjectId(topic_id)
        except Exception:
            return jsonify({"error": "Invalid ObjectId format"}), 400

        topic = mongo.db.mcq.find_one({"_id": obj_id})
        if not topic:
            return jsonify({"error": "Topic not found"}), 404

        # Convert ObjectId to string for JSON serialization
        topic["_id"] = str(topic["_id"])
        return jsonify(topic), 200

    @mcq_blueprint.route("/create-topic", methods=["POST"])
    def create_topic():
        print("creating topic..")
        try:
            data = request.get_json()
            print(data)

            # Validate against schema
            schema = TopicSchema()

            try:
                data = schema.load(request.json)
                print("data" + str(data))

                result = mongo.db.mcq.insert_one(data)
                print("result: " + str(result))

                saved_object = mongo.db.mcq.find_one({"_id": result.inserted_id})
                print("saved_object: " + str(saved_object))
                return (
                    jsonify(
                        {
                            "message": "Quiz added successfully",
                            "inserted_id": str(saved_object["_id"]),
                            "topic": str(saved_object["topic"]),
                        }
                    ),
                    201,
                )
            except ValidationError as err:
                print("error 400")
                return jsonify({"errors": err.messages}), 400

        except ValidationError as e:
            return jsonify({"error": f"Validation failed: {e.message}"}), 400

    return mcq_blueprint
