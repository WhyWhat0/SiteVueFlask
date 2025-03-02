from flask import Flask, Response, render_template,jsonify, request, json
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

messageTemplate ={
    'id': '',
    'text': '',
    'date': '',
    'files': [],
    'isMyMessage': '',
}

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
            'isMyMessage': 1,
        })
        textAnswer = getMessagefromBot(post_data.get('text'))
        
        answersBot.append({
            'id': post_data.get('id')+1,
            'text': textAnswer,
            'date': post_data.get('date'),
            'files': [],
            'isMyMessage': 0,
        })
        response_object['message'] = 'message added!'
    return jsonify(response_object)


@app.route('/bot', methods=['GET'])
def botGetFun():
    response_object = {'status': 'success'}
    response_object['messagesList'] = messagesBot
    response_object['answersList'] = answersBot
    formatted_json = json.dumps(response_object, indent=4, sort_keys=True, ensure_ascii=False)
    
    # Возвращаем кастомизированный ответ
    return Response(formatted_json, mimetype='application/json; charset=utf-8')

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
