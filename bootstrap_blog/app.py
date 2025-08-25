from flask import Flask,render_template
import requests

app = Flask(__name__)
# API URL || To use the data.
API_URL = "https://api.npoint.io/bd8938422b0310f65538"
response = requests.get(API_URL)
data = response.json()

@app.route("/")
def home():
    return render_template("index.html",data=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)