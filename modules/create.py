import os

from flask import Flask, render_template, request
from models import models

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://python_user:MyPassw0rd#1@localhost/python_db" # os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
