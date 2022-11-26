from flask import Blueprint, request
import requests

from utils import HEADERS, load_file_config


user_blueprints = Blueprint('user_blueprints', __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-security') + "/user"


@user_blueprints.route("/users", methods=['GET'])
def get_all_users() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@user_blueprints.route("/user/<int:id_>", methods=['GET'])
def get_user_by_id(id_: int) -> dict:
    url = f'{url_base}/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@user_blueprints.route("/user/insert", methods=['POST'])
def insert_user() -> dict:
    user = request.get_json()
    url = f'{url_base}/insert'
    response = requests.post(url, headers=HEADERS, json=user)
    return response.json()


@user_blueprints.route("/user/update/<int:id_>", methods=['PUT'])
def update_user(id_: int) -> dict:
    user = request.get_json()
    url = f'{url_base}/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=user)
    return response.json()


@user_blueprints.route("/user/delete/<int:id_>", methods=['DELETE'])
def delete_user(id_: int):
    url = f'{url_base}/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return {"message": "processed"}, response.status_code
