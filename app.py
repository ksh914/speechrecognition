import ssl
from flask import Flask, render_template, request, redirect
import speech_recognition as sr


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index3():
    return render_template('speechToText.html')


if __name__ == "__main__":
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem', password='louie')
    app.run(host="0.0.0.0", port=5000, ssl_context=ssl_context, debug=True)
