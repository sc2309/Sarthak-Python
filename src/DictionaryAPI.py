import requests
from flask import Blueprint,request,jsonify, render_template
import speech_recognition as sr
import os
from dotenv import load_dotenv

load_dotenv()

DictionaryAPI = Blueprint('DictionaryAPI', __name__)

@DictionaryAPI.route('/dictionary', methods=['GET'])
def index():
    return render_template('Dictionary.html')

@DictionaryAPI.route('/get_api', methods=['GET'])
def DictionaryAPIcall():
    user_value = request.args.get('user_value')
    #headers = {'Accept': 'application/json'}
    #data = request.form.get('data')
    #word = data.get('word')
    DICTIONARY_API = os.environ.get('DICTIONARY_API')
    api_url = DICTIONARY_API+user_value
    r = requests.get(api_url)
    getData = r.json()
    #response_data = {'message': 'Data received successfully', 'received_data': getData}
    return jsonify(getData)