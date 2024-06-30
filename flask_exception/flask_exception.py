import json
import logging
import traceback
from datetime import datetime

from flask import current_app, request
from werkzeug.exceptions import HTTPException


class FlaskException:
    """Enable Save exception to DB for a Flask app.

    ::

        app = Flask(__name__)
        app.config['FLASK_EXCEPTION_APP_NAME'] = 'FLASK'
        app.config['FLASK_EXCEPTION_ADD_TO_DB_FUNC'] = add_to_db
        app.config['FLASK_EXCEPTION_OBJ_OF_LOGGER'] = logging.getLogger('FLASK_EXCEPTION')
        fe = FlaskException(app)


    """

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.extensions["FLASK_EXCEPTION"] = self
        app.config.setdefault("FLASK_EXCEPTION_APP_NAME", "FLASK")
        if not app.config["FLASK_EXCEPTION_ADD_TO_DB_FUNC"]:
            raise ValueError("FLASK_EXCEPTION_ADD_TO_DB_FUNC is not set.")

        if not callable(app.config["FLASK_EXCEPTION_ADD_TO_DB_FUNC"]):
            raise ValueError("FLASK_EXCEPTION_ADD_TO_DB_FUNC is not callable.")

        if not isinstance(app.config["FLASK_EXCEPTION_OBJ_OF_LOGGER"], logging.Logger):
            flask_logger = logging.getLogger("FLASK_EXCEPTION")
        else:
            flask_logger = app.config["FLASK_EXCEPTION_OBJ_OF_LOGGER"]

        @app.errorhandler(HTTPException)
        def handle_exception(e):
            """Return JSON instead of HTML for HTTP errors."""
            # start with the correct headers and status code from the error
            response = e.get_response()
            # replace the body with JSON
            response.data = json.dumps(
                {
                    "code": e.code,
                    # "name": e.name,
                    "error": e.description,
                }
            )
            response.content_type = "application/json"
            flask_logger.error(response.data)

            return response

        @app.errorhandler(Exception)
        def exception_logger(e):
            """Log the exception."""
            if issubclass(type(e), HTTPException):
                # Do not log HTTPException
                return handle_exception(e)

            flask_logger.error(str(e), exc_info=traceback.format_exc())
            current_app.config["FLASK_EXCEPTION_ADD_TO_DB_FUNC"](
                current_app.config["FLASK_EXCEPTION_APP_NAME"],
                method=request.method,
                endpoint=request.endpoint,
                host=request.host,
                url=request.url,
                args=request.args,
                data=request.data,
                failed_date=datetime.now(),
                exception=str(e),
                trace=traceback.format_exc(),
            )
            data = {
                "code": 500,
                # "name": e.name,
                "error": "Internal Server Error.",
            }
            return data, 500
