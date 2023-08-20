from flask import Flask

def myFirstApp():
    app = Flask(__name__)
    from views import views
    from auth import auth
    from speech import speech
    from DictionaryAPI import DictionaryAPI
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(speech, url_prefix='/')
    app.register_blueprint(DictionaryAPI, url_prefix='/')
    return app

app = myFirstApp()
app.run(debug=True)