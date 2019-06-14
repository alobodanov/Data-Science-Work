# import necessary libraries
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo

import scrape_mars

# create instance of Flask app
app = Flask(__name__)
mongo = PyMongo(app)


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape", method=['GET'])
def scrape():
    print('test')
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )

    return render_template('index.html', mars=mars_data)


if __name__ == "__main__":
    app.run(debug=True)
