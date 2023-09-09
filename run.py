# The code is importing the `app` object from the `app` module. It is also importing the `models` and
# `db` objects from the `app` module.
from app import app
from app import models, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=8080)
