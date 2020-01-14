import os
import json
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo, pymongo

from bson.objectid import ObjectId 

app = Flask(__name__)
app.secret_key = "some_secret"

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = "mongodb+srv://root:Thisisarandompassword@myfirstcluster-qpzww.mongodb.net/theRecipe?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/", methods=["GET", "POST"]) 
def index():

     return render_template("index.html")

@app.route("/NoResults")
def noresult(): 

     return render_template("noresult.html")


@app.route("/results", methods=["GET", "POST"])

def results():

    collection = mongo.db.Recipes
    if request.method == 'POST':
        searching = request.form['search']
        if searching > "":

            test = 0

            results = collection.find({"name": {"$regex": searching, "$options": "i"}})
            for result in results:
                if result != "":
                    test = test + 1

            if test != 0:

                return render_template("results.html", search = collection.find({"name": {"$regex": searching, "$options": "i"}}))
   
            else:
                return render_template("noresult.html")

        if searching == "":
            return render_template("results.html", search = collection.find())

        else:
            return render_template("noresult.html")

@app.route("/insert", methods=["GET", "POST"])

def insert():
    collection = mongo.db.Recipes
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        picture = request.form['picture']
        if name > "" and ingredients > "" and instructions > "" and picture > "":

            collection.insert({'name': name, 'ingredients': ingredients, 'directions': instructions, 'image': picture})

            return render_template("insert.html")
    
    return ('', 204)

@app.route("/email", methods=["GET", "POST"])

def email():
    collection = mongo.db.email
    if request.method == 'POST':
        email = request.form['inputEmail']
       
        if email > "":

            collection.insert({'email': email})

            return render_template("insertEmail.html")
    
    return ('', 204)
   


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port = int(os.environ.get('PORT', '5000')),
            debug=True)

