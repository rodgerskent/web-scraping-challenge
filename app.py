#app
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
from webdriver_manager.chrome import ChromeDriverManager

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/marsmission")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    # Find one record of data from the mongo database
    info = mongo.db.missiontools.find_one()
    # Return template and data
    return render_template("index.html", info=info)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # Update the Mongo database using update and upsert=True
    info = mongo.db.missiontools
    featuretext = scrape_mars.scrapemars()
    print(featuretext)
    mongo.db.missiontools.update({}, featuretext, upsert=True)
    return redirect("/", code=302)
 
if __name__ == "__main__":
    app.run(debug=True)






