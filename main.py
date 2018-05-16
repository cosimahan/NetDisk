from flask import Flask, render_template
import os
import flask_sqlalchemy
import sqlite3
import nd_config,db_model


app = Flask(__name__)
app.config.from_object('nd_config.FlaskConfig')
db = flask_sqlalchemy.SQLAlchemy(app)

@app.route('/')
def home():
    t = db_model.User.query.filter().all()
    return render_template("home.html", t=str(t[0].user_password))

@app.route('/module/register')
def module_register():
    return render_template("module/register.html",)


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=80)
