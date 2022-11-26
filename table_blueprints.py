from flask import Blueprint, request
import requests

from utils import HEADERS, load_file_config


table_blueprints = Blueprint('table_blueprints', __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-academic') + "/table"


@table_blueprints.route("/tables", methods=['GET'])
def get_all_tables() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@table_blueprints.route("/table/<string:id_>", methods=['GET'])
def get_table_by_id(id_: str) -> dict:
    url = f'{url_base}/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@table_blueprints.route("/table/insert", methods=['POST'])
def insert_table() -> dict:
    table = request.get_json()
    url = f'{url_base}/insert'
    response = requests.post(url, headers=HEADERS, json=table)
    return response.json()


@table_blueprints.route("/table/update/<string:id_>", methods=['PUT'])
def update_table(id_: str) -> dict:
    table = request.get_json()
    url = f'{url_base}/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=table)
    return response.json()


@table_blueprints.route("/table/delete/<string:id_>", methods=['DELETE'])
def delete_table(id_: str):
    url = f'{url_base}/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return {"message": "processed"}, response.status_code
