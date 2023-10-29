from flask import Flask
from cx_Freeze import setup, Executable

executables = [Executable('app.py')]
options = {
    'build_exe': {
        'includes': ['pyttsx3', 'flask', 'speech_recognition', 'openpyxl', 'requests', 'dotenv', 'os'], #additional files or data program needs
    }
}

setup(
    name="app",
    version="1.0",
    description="A WEB-APPLICATION",
    executables=executables,
    options=options
)

def myFirstApp():
    app = Flask(__name__)
    from views import views
    from auth import auth
    from speech import speech
    from DictionaryAPI import DictionaryAPI
    from python import python
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(speech, url_prefix='/')
    app.register_blueprint(DictionaryAPI, url_prefix='/')
    app.register_blueprint(python, url_prefix='/')
    return app

app = myFirstApp()
app.run(debug=True)