from flask import Flask
from flask import render_template
from Flaskext.mysql import MySQL

app = Flask(__name__)
mysql=MySQL()

if __name__ == "__name__":
     app.run(debug=True)