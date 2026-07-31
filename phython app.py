from flask import Flask, render_template, request

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        msg = request.form["message"]

        message = f"Thank you {name}! Your message has been received."

    return render_template("index.html", message=message)

if _name_ == "_main_":
    app.run(debug=True)