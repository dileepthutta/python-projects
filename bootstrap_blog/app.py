from flask import Flask,render_template,request
import requests,smtplib

app = Flask(__name__)
# API URL || To use the data.
API_URL = "https://api.npoint.io/9a26c380138981bcfd89"
response = requests.get(API_URL)
data = response.json()


# Home Route.
@app.route("/")
def home():
    return render_template("index.html",data=data)

#About Route.
@app.route("/about")
def about():
    return render_template("about.html")

#Contact route with functionality
@app.route("/contact",methods=["POST","GET"])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        data={
            "name":name,
            "email":email,
            "phone":phone,
            "message":message
        }
        # for item in data.values():
        #     print(item)

        # Sends email when the form is submitted.
        my_email = ""  # ✅ Fill in your Gmail address
        password = ""  # ✅ Use App Password, not regular password
        recipient_email = ""  # ✅ Fill in the recipient's address
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # ✅ Specify port 587
            connection.starttls()  # ✅ Start TLS encryption
            connection.login(user=my_email, password=password)  # ✅ Use correct login credentials
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient_email,
                msg="Subject:Blog Page\n\n"
                    f"Name :    {name}\n"
                    f"Email :   {email}\n"
                    f"Phone :   {phone}\n"
                    f"Message:  {message}\n"
            )

        return render_template("contact.html",msg_sent=True)
    else:
        return render_template("contact.html",msg_sent=False)


# Post route
@app.route("/post/<int:num>")
def post(num):
    requested_post = next((posts for posts in data if posts["id"] == num), None)
    return render_template("post.html",post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)