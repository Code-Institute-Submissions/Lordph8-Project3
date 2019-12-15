import os
import json
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.secret_key = "some_secret"

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = "mongodb+srv://root:Thisisarandompassword@myfirstcluster-qpzww.mongodb.net/theRecipe?retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route("/", methods=["GET", "POST"])
def index():
    
    return render_template("index.html", search=mongo.db.Recipes.find())

@app.route('/results')
def get_recipes():
    return render_template("index.html", search=mongo.db.Recipes.find())
    if search > "":
        for i in search.ingredients:
            i.replace(",", "<br>")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port = int(os.environ.get('PORT', '5000')),
            debug=True)