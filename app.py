import ssl
from flask import Flask, render_template, request, redirect
import speech_recognition as sr


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index3():
    return render_template('speechToText.html')


if __name__ == "__main__":

    app.run('0.0.0.0', port=5000, debug=True)
