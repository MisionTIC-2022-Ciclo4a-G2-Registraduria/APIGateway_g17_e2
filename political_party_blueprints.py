from flask import Blueprint, request
import requests

from utils import HEADERS, load_file_config

political_party_blueprints = Blueprint("political_party_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get("url-backend-results") + "/political_party"


@political_party_blueprints.route("/political_partys", methods=["GET"])
def get_all_political_parties() -> dict:
    url = f"{url_base}/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@political_party_blueprints.route("/political_party/<string:id_>", methods=["GET"])
def get_political_party_by_id(id_: str) -> dict:
    url = f"{url_base}/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@political_party_blueprints.route("/political_party/insert", methods=["POST"])
def insert_political_party() -> dict:
    political_party = request.get_json()
    url = f"{url_base}/insert"
    response = requests.post(url, headers=HEADERS, json=political_party)
    return response.json()


@political_party_blueprints.route("/political_party/update/<string:id_>", methods=["PUT"])
def update_political_party(id_: str) -> dict:
    political_party = request.get_json()
    url = f"{url_base}/update/{id_}"
    response = requests.patch(url, headers=HEADERS, json=political_party)
    return response.json()


@political_party_blueprints.route("/political_party/delete/<string:id_>", methods=["DELETE"])
def delete_political_party(id_: str) -> dict:
    url = f"{url_base}/delete/{id_}"
    response = requests.delete(url, headers=HEADERS)
    return response.get()


