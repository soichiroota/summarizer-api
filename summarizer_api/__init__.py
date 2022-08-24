import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension

# instantiate the extensions
toolbar = DebugToolbarExtension()
bootstrap = Bootstrap()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS", "summarizer_api.config.ProductionConfig")
    app.config.from_object(app_settings)

    # set up extensions
    toolbar.init_app(app)
    bootstrap.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # register blueprints
    from summarizer_api.application.health_checks.views import health_check_blueprint
    from summarizer_api.application.summpy.views import summpy_blueprint
    from summarizer_api.application.pysummarization.views import pysummarization_blueprint
    from summarizer_api.application.sumy.views import sumy_blueprint

    app.register_blueprint(health_check_blueprint)
    app.register_blueprint(summpy_blueprint, url_prefix="/api")
    app.register_blueprint(pysummarization_blueprint, url_prefix="/api")
    app.register_blueprint(sumy_blueprint, url_prefix="/api")

    return app
