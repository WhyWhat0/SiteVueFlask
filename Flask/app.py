from flask import Flask, render_template,jsonify, request
from flask_cors import CORS, cross_origin
from bot import *
import time

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app)
messagesBot = []
answersBot = []
messagesHuman = []

@app.route('/bot', methods=['POST'])
def botPostFun():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        messagesBot.append({
            'id': post_data.get('id'),
            'text': post_data.get('text'),
            'date': post_data.get('date'),
            'files': post_data.get('files'),
            'isMyMessage': 'true',
        })
        answer = getMessagefromBot(post_data.get('text'))
        answersBot.append(answer)
        response_object['message'] = 'message added!'
    return jsonify(response_object)


@app.route('/bot', methods=['GET'])
def botGetFun():
    response_object = {'status': 'success'}
    response_object['messageList'] = messagesBot
    response_object['answersList'] = answersBot
    return jsonify(response_object)


@app.route('/human', methods=['GET', 'POST'])
@cross_origin()
def humanFun():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        print(request.form)
        post_data = request.get_json()
        messagesHuman.append({
            'id': post_data.get('id'),
            'text': post_data.get('text'),
            'date': post_data.get('date'),
            'files': post_data.get('files'),
            'isMyMessage': post_data.get('isMyMessage'),
        })
        response_object['message'] = 'message added!'
    else:
        response_object['messageList'] = messagesHuman
#     return jsonify(response_object)
@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
