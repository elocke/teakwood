from flask import Flask
# from flask.ext.mongoengine import MongoEngine
from flask import render_template

# from flask_bootstrap import Bootstrap, WebCDN
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.bower import Bower

import datetime
# import mongoengine
from eve import Eve
# from eve_mongoengine import EveMongoengine

# import views
from flask import make_response
import os 

print os.getcwd()
from bson.objectid import ObjectId
import json 

app = Eve(__name__,settings='/code/app/settings.py')

def countArtistShowCt(items):
    print items
    for item in items:
        if item['_status'] == 'OK':
            artists = app.data.driver.db['artists']
            shows = app.data.driver.db['shows']
            artist_id = ObjectId(item['artist'])
            artist = artists.find_one({'_id': artist_id})
            count = shows.find({'artist': artist_id}).count()
            url = '/api/artists/' + str(artist_id)
            etag = str(artist['_etag'])
            print artist_id, count, artist, url, etag
            r = app.test_client().patch(url, data={"show_count": count}, content_type='application/json', headers={'IF_MATCH': etag})
            print r.status_code, r.headers, r.data


def debugPatch(item, original):
    print item


app.on_inserted_shows += countArtistShowCt
app.on_update_artists += debugPatch



import logging
from logging import FileHandler
from logging import Formatter
file_handler = FileHandler('../logs/flask.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
app.logger.addHandler(file_handler)



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
app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
app.debug = True
app.url_map.strict_slashes = False

# Setup Bootstrap
# Bootstrap(app)
# app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
#     '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/'
# )
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