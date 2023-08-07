from flask import Blueprint, render_template
import speech_recognition as sr

speech = Blueprint('speech', __name__)

@speech.route('/login')
def index():
    return render_template('login.html')

@speech.route('/recognize', methods=['POST'])
def recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return render_template('login.html', text=text)
        except sr.UnknownValueError:
            return render_template('login.html', error="Could not understand audio")
        except sr.RequestError as e:
            return render_template('login.html', error=f"Could not request results; {e}")
        