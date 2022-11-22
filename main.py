from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token, verify_jwt_in_request,
                                get_jwt_identity)
import requests as rq
from waitress import serve
from datetime import timedelta

import utils
from candidate_blueprints import candidate_blueprints
from political_party_blueprints import political_party_blueprints
from vote_blueprints import vote_blueprints
from permission_blueprints import permission_blueprints
from rol_blueprints import rol_blueprints
from table_blueprints import table_blueprints
from user_blueprints import user_blueprints


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "mision_tic_g17"
cors = CORS(app)
jwt = JWTManager(app)
app.register_blueprint(candidate_blueprints)
app.register_blueprint(political_party_blueprints)
app.register_blueprint(vote_blueprints)
app.register_blueprint(permission_blueprints)
app.register_blueprint(rol_blueprints)
app.register_blueprint(table_blueprints)
app.register_blueprint(user_blueprints)


@app.before_request
def before_request_callback() -> tuple:
    endpoint = utils.clear_url(request.path)
    exclude_routes = ["/", "/login"]
    if exclude_routes.__contains__(request.path):
        pass
    elif verify_jwt_in_request():
        user = get_jwt_identity()
        if user.get("rol"):
            has_grant = utils.validate_grant(endpoint, request.method, user["rol"].get("idRol"))
            if not has_grant:
                return {"message": "Access denied by grant"}, 401
        else:
            return {"message": "Access denied by left rol"}, 401


@app.route("/", methods=["GET"])
def home() -> dict:
    response = {"message": "Welcome to the Electoral API Gateway "}
    return response


@app.route("/login", methods=["POST"])
def login() -> tuple:
    user = request.get_json()
    url = data_config.get('url-backend-security') + "/user/login"
    response = rq.post(url, headers=utils.HEADERS, json=user)
    if response.status_code == 200:
        user_logged = response.json()
        del user_logged["rol"]["permissions"]
        expires = timedelta(days=1)
        access_token = create_access_token(identity=user_logged, expires_delta=expires)
        return {"token": access_token, "user_id": user_logged.get("id")}, 200
    else:
        return {"message": "Access denied"}, 401


if __name__ == '__main__':
    data_config = utils.load_file_config()
    print(f'API GATEWAY Server Running...: http://{data_config.get("url-api-gateway")}' +
          f':{data_config.get("port")}')
    serve(app, host=data_config.get("url-api-gateway"), port=data_config.get("port"))
