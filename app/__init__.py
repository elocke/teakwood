from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask_bootstrap import Bootstrap, WebCDN


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "teakwood"}
# app.config["MONGODB_DB"] =
# app.config["MONGODB_USERNAME"] =
# app.config["MONGODB_PASSWORD"] =
# app.config["MONGODB_HOST"] =
# app.config["MONGODB_PORT"] =

app.config["SECRET_KEY"] = "r@g3f@c3"

db = MongoEngine(app)


# Setup Bootstrap
Bootstrap(app)
app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
    '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/'
)


if __name__ == '__main__':
    app.run()
