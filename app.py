from flask import Flask
from datetime import datetime

def myFirstApp():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    app = Flask(__name__)
    from src.views import views
    from src.auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

app = myFirstApp()

if __name__ == '__main__':
    app.run(debug=True)