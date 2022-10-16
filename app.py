from flask import Flask
from models import db
from routes import api

app = Flask(__name__)
api.init_app(app)
app.config.from_object('config.Config')
db.init_app(app)

if __name__ == '__main__':
    app.run(host = '127.0.0.1')