import os
from flask import Flask

# Initialize application
app = Flask(__name__, static_folder=None)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)