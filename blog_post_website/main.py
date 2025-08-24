from flask import Flask, render_template
import requests

blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_endpoint)
posts = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route("/blog/<int:num>")
def blog(num):
    # Find the post with matching id
    requested_post = next((post for post in posts if post["id"] == num), None)
    print(type(requested_post))
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
