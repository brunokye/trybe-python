from bson import ObjectId
from flask import Blueprint, jsonify, request
from models.joke_model import JokeModel
from .status_http import StatusHttp

jokes_controller = Blueprint("jokes", __name__)


def _get_all_jokes():
    jokes = JokeModel.find()
    return [joke.to_dict() for joke in jokes]


def _get_joke(id: str):
    return JokeModel.find_one({"_id": ObjectId(id)})


@jokes_controller.route("/", methods=["GET"])
def joke_index():
    jokes_list = _get_all_jokes()
    return jsonify(jokes_list)


@jokes_controller.route("/random", methods=["GET"])
def joke_random():
    joke = JokeModel.get_random()

    if joke is None:
        return jsonify({"error": "No jokes available"}), 404

    return jsonify(joke.to_dict()), StatusHttp.OK


@jokes_controller.route("/", methods=["POST"])
def joke_post():
    new_joke = JokeModel(request.json)
    new_joke.save()
    return jsonify(new_joke.to_dict()), StatusHttp.CREATED


@jokes_controller.route("/<id>", methods=["PUT"])
def joke_update(id: str):
    joke = _get_joke(id)

    if joke is None:
        return jsonify({"error": "Joke not found"}), StatusHttp.NOT_FOUND

    joke.update(request.json)
    return jsonify(joke.to_dict()), StatusHttp.OK


@jokes_controller.route("/<id>", methods=["GET"])
def joke_show(id: str):
    joke = _get_joke(id)

    if joke is None:
        return jsonify({"error": "Joke not found"}), StatusHttp.NOT_FOUND

    return jsonify(joke.to_dict()), StatusHttp.OK


@jokes_controller.route("/<id>", methods=["DELETE"])
def joke_delete(id: str):
    joke = _get_joke(id)

    if joke is None:
        return jsonify({"error": "Joke not found"}), StatusHttp.NOT_FOUND

    joke.delete()
    return jsonify(joke.to_dict()), StatusHttp.NO_CONTENT
