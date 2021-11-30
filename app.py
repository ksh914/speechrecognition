from flask import Flask, render_template, request, redirect
import speech_recognition as sr


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index3():
    transcript=""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("말씀하세요")
        audio = r.listen(source)
    try:
        transcript = r.recognize_google(audio, language="ko-KR")
        print(transcript)
    except sr.UnknownValueError:
        print("다시 말씀해 주세요")
    except sr.RequestError as e:
        print("결과값을 불러오지 못했습니다.; {0}".format(e))
    return render_template('index3.html', transcript=transcript)


if __name__ == "__main__":
    app.run('0.0.0.0', port=5001, debug=True)
