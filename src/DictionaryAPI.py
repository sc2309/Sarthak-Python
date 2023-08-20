import requests
from flask import Blueprint,request,jsonify, render_template
import speech_recognition as sr

DictionaryAPI = Blueprint('DictionaryAPI', __name__)

@DictionaryAPI.route('/dictionary', methods=['GET'])
def index():
    return render_template('Dictionary.html')

@DictionaryAPI.route('/get_api', methods=['GET'])
def DictionaryAPIcall():
    data = request.json
    html_value = data.get('htmlValue')
    #headers = {'Accept': 'application/json'}
    #data = request.form.get('data')
    #word = data.get('word')
    api_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'+html_value
    r = requests.get(api_url)
    getData = r.json()
    #response_data = {'message': 'Data received successfully', 'received_data': getData}
    return getData