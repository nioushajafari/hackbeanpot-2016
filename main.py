from flask import Flask, render_template
from model import HouseHold
import json
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/sendSass")
def sendSass():
    return render_template('sendSass.html', name="James")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/household")
def household():
    houseHold = HouseHold("fake", 6)
    houseHold.addUser("Jaclyn")
    houseHold.addUser("NJ")
    houseHold.addUser("Adrian")
    houseHold.addUser("Ali")
    houseHold.addUser("Spencer")
    houseHold.addUser("James")

    return json.dumps(houseHold.__dict__)


if __name__ == "__main__":
    app.run(debug=True)

