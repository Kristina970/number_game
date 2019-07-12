from flask import Flask

from db import db
from config import run_config
from create_db import create_db

app = Flask(__name__)


def run_app():
    app.config.from_object(run_config())

    db.init_app(app)
    app.register_blueprint(create_db)

    return app


@app.route('/_health')
def health_check():
    return 'status 200'


if __name__ == '__main__':
    app.run(debug=True)


