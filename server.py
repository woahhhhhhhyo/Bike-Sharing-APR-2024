from flask import Flask, render_template
from flask import jsonify
import connexion


# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("master.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)

@app.route("/html/<page>")
def html_hello(page):
    return render_template(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
