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

@app.route("/")
def index():

     return render_template("index.html")

@app.route("/NoResults")
def noresult():

     return render_template("noresult.html")


@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == 'POST':
        searching = request.form['search']
        if searching > "":
        
            return render_template("results.html", section="section", search=mongo.db.Recipes.find({"name": searching}))

        else:
            return render_template("noresult.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port = int(os.environ.get('PORT', '5000')),
            debug=True)

"""
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        search = request.form['search']
        if request.method == 'POST':
            return search_results(search)
        return render_template('index.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    if search.data['search'] == '':
        qry = mongo.db.Recipesy(name)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results) 
"""