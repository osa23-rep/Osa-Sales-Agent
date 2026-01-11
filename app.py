from flask import Flask, render_template, request
from tools import recommend_phone_upgrade  # type: ignore # uses your function

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    # Show the form page
    return render_template("index.html")

@app.route("/phone", methods=["POST"])
def phone():
    # Read form values (they come in as strings)
    budget = int(request.form.get("budget", "600"))
    preference = request.form.get("preference", "android")
    priority = request.form.get("priority", "value")
    trade_in = request.form.get("trade_in", "no") == "yes"
    condition = request.form.get("condition", "good")

    # Call your recommendation logic
    result = recommend_phone_upgrade(budget, preference, priority, trade_in, condition)

    # Show the results page
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
