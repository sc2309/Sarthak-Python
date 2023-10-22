from flask import Blueprint, request, render_template

python = Blueprint('python', __name__)

@python.route('/python', methods=['GET', 'POST'])
def learnPython():
    head = 'hello world!'
    return render_template('python.html', headtype=head)
