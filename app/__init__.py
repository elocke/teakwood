from flask import Flask
# from flask.ext.mongoengine import MongoEngine
from flask import render_template

from flask_bootstrap import Bootstrap, WebCDN
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.bower import Bower

import datetime
# import mongoengine
from eve import Eve
# from eve_mongoengine import EveMongoengine

# import views
from flask import make_response
import os 

print os.getcwd()

app = Eve(__name__,settings='settings.py')
# app.on_fetched_resource_artists += count_shows

def format_exception(tb):
    res = make_response(tb.render_as_text())
    res.content_type = 'text/plain'
    return res
app.jinja_env.exception_formatter = format_exception

app.config["MONGODB_SETTINGS"] = {
    "host": "database",
    "port": 27017,
	"db": "teakwood"
	}

app.config["SECRET_KEY"] = "r@g3f@c3"

app.config['DEBUG_TB_PANELS'] = (
    'flask.ext.debugtoolbar.panels.versions.VersionDebugPanel',
    'flask.ext.debugtoolbar.panels.timer.TimerDebugPanel',
    'flask.ext.debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask.ext.debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask.ext.debugtoolbar.panels.template.TemplateDebugPanel',
    'flask.ext.debugtoolbar.panels.logger.LoggingPanel'
    # 'flask.ext.mongoengine.panels.MongoDebugPanel'
)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True
app.url_map.strict_slashes = False

# Setup Bootstrap
Bootstrap(app)
app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
    '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/'
)
Bower(app)

# from flask.ext.assets import Environment, Bundle
# assets = Environment(app)
# assets.init_app(app)
# css_all = Bundle(
    # 'less/style.less',
    # filters='less, cssmin',
    # output='gen/min.css',
# )

# These assets get passed templates to be rendered
# assets.register('css_all', css_all)
# assets.debug = True
# app.config['ASSETS_DEBUG'] = True


from rq_dashboard import RQDashboard

app.config["REDIS_HOST"] = "redis"
RQDashboard(app)

toolbar = DebugToolbarExtension(app)

from flask.ext.triangle import Triangle
Triangle(app)


from views.main import main
from views.partials import partials
# # Blueprints
app.register_blueprint(main, url_prefix='/', template_folder='templates')
app.register_blueprint(partials, url_prefix='/partials', template_folder='templates')


if __name__ == '__main__':
    app.run()