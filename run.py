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

    if request.method == 'POST':
        search = request.form['search']#form input on initial position
        
        return render_template("index.html", search=mongo.db.Recipes.find({ "name": search }))


@app.route('/results')
def get_recipes():
    if request.method == 'POST':
        search = request.form['search']#form input on initial position
        
        return render_template("index.html", search=mongo.db.Recipes.find({ "name": search }))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port = int(os.environ.get('PORT', '5000')),
            debug=True)