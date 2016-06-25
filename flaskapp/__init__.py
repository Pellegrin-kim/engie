
from flask import Flask, render_template
from flask import url_for
from functools import wraps
from flask import request, Response
import os
from flask import redirect
from werkzeug import secure_filename
from flask import send_from_directory

app = Flask(__name__)


@app.route('/')
def main():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)


@app.route('/map')
def main():
    try:
        return render_template("map.html")
    except Exception as e:
        return str(e)


@app.route('/conseil')
def main():
    try:
        return render_template("conseil.html")
    except Exception as e:
        return str(e)


@app.route('/evolution')
def main():
    try:
        return render_template("evolution.html")
    except Exception as e:
        return str(e)

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)

