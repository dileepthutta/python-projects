from flask import Flask,render_template
import requests

app = Flask(__name__)
# API URL || To use the data.
API_URL = "https://api.npoint.io/9a26c380138981bcfd89"
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

@app.route("/post/<int:num>")
def post(num):
    requested_post = next((posts for posts in data if posts["id"] == num), None)
    return render_template("post.html",post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)