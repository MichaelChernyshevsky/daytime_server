from flasgger import Swagger

from packages.exports import *
from common.user.api.index import user_bp
from common.packages.api.index import packages_bp


def register_blueprints(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(packages_bp)
    # packages
    app.register_blueprint(task_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(timer_bp)
    app.register_blueprint(economy_bp)





    





def register_swagger(app):
    SWAGGER_TEMPLATE = {
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "\JWT access token"
            }
        }
    }
    swag = Swagger(app, template=SWAGGER_TEMPLATE)
    app.config["SWAGGER"] = {
        "openapi": "3.0.0",
        "title": "Daytime api",
        "description": ""
    }