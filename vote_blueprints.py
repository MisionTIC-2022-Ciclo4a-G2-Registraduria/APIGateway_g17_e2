from flask import Blueprint, request
import requests

from utils import HEADERS, load_file_config

vote_blueprints = Blueprint("vote_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get("url-backend-results") + "/vote"


@vote_blueprints.route("/votes", methods=["GET"])
def get_all_votes() -> dict:
    url = f"{url_base}/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@vote_blueprints.route("/vote/<string:id_>", methods=["GET"])
def get_vote_by_id(id_: str) -> dict:
    url = f"{url_base}/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@vote_blueprints.route("/vote/insert", methods=["POST"])
def insert_vote() -> dict:
    vote = request.get_json()
    url = f"{url_base}/insert"
    response = requests.post(url, headers=HEADERS, json=vote)
    return response.json()


@vote_blueprints.route("/vote/update/<string:id_>", methods=["PUT"])
def update_vote(id_: str) -> dict:
    vote = request.get_json()
    url = f"{url_base}/update/{id_}"
    response = requests.patch(url, headers=HEADERS, json=vote)
    return response.json()


@vote_blueprints.route("/vote/delete/<string:id_>", methods=["DELETE"])
def delete_vote(id_: str) -> dict:
    url = f"{url_base}/delete/{id_}"
    response = requests.delete(url, headers=HEADERS)
    return response.get()


