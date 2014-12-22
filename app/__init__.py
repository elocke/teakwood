from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask_bootstrap import Bootstrap, WebCDN
from flask_debugtoolbar import DebugToolbarExtension

# import mongoengine
from eve import Eve
from eve_mongoengine import EveMongoengine

# import views


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"HOST": "database",
	"DB": "teakwood"
	}

# app.config["MONGODB_DB"] =
# app.config["MONGODB_USERNAME"] =
# app.config["MONGODB_PASSWORD"] =
# app.config["MONGODB_HOST"] =
# app.config["MONGODB_PORT"] =

app.config["SECRET_KEY"] = "r@g3f@c3"

app.config['DEBUG_TB_PANELS'] = (
    'flask.ext.debugtoolbar.panels.versions.VersionDebugPanel',
    'flask.ext.debugtoolbar.panels.timer.TimerDebugPanel',
    'flask.ext.debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask.ext.debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask.ext.debugtoolbar.panels.template.TemplateDebugPanel',
    'flask.ext.debugtoolbar.panels.logger.LoggingPanel',
    'flask.ext.mongoengine.panels.MongoDebugPanel'
)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True


# Setup Bootstrap
Bootstrap(app)
# app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
#     '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/'
# )

db = MongoEngine(app)
db.init_app(app)


from rq_dashboard import RQDashboard

app.config["REDIS_HOST"] = "redis"
RQDashboard(app)

toolbar = DebugToolbarExtension(app)

# default eve settings
my_settings = {
    'MONGO_HOST': 'database',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'teakwood',
    'DOMAIN': {'eve-mongoengine': {}}, # sadly this is needed for eve
    'URL_PREFIX': 'api'
}

from models import Artist, Show, File
app = Eve(settings=my_settings)
# init extension
ext = EveMongoengine(app)
# register model to eve
ext.add_model(Artist)


from app.views import dashboard
# Blueprints
app.register_blueprint(dashboard.dashboard)

if __name__ == '__main__':
    app.run()
