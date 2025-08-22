from flask import Flask
import random

app = Flask(__name__)

#Home Route
@app.route("/")
def home():
    return ("<h1 style= text-align:center>Guess a number between 1 to 10</h1> "
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZW90MGNkOGlqOXF3Nnp0M3puYWtmYmwwN2FmbHc1eXhrYXN1OXl1ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UDU4oUJIHDJgQ/giphy.gif'/>")

# Guessing a Number route
@app.route("/<int:num>")
def guess_num(num):
    randint = random.randint(0,10)
    if num > randint:
        return ("<h1 style= text-align:center color:red>Too high</h1>"
                "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYm8xa2tremd4b2FmcmV5MDhod2QwOGRta3luZnZoc3plbDdydHgzcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CIa2q86HbmclbNvOg8/giphy.gif'/>")
    elif num < randint:
        return ("<h1 style= text-align:center >Too low</h1>"
                "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXo4b3dyZWxyZjBpZHA1ZTB5cmNjdHUwZWxoN29udmRiYWQ1cnd4aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Isoke76D17mNI02sve/giphy.gif'/>")
    else:
        return ("<h1 style= text-align:center >Correct guess</h1>"
                "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnQ1ODV1Mmttbmtpb3h6ZXUwM3c4enlkcXlmMzMxbWQyYnB6Z3B4dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Eb2Y9fGH4Tu3vlFTsp/giphy.gif'/>")

if __name__ == "__main__":
    app.run(debug=True)
