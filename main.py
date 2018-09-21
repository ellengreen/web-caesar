from flask import Flask, render_template
from caesar import rotate_string

app = Flask(__name__)

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>

      <!-- create your form here -->

    </body>
</html>

"""

@app.route("/")
def index():
    return "Hello World"


app.run(debug = True)


