from flask import Flask, render_template
import time
import requests

TOKEN = '7639535623:AAFFSzVZFohN2JtjIsGRn1TP-4YEdPZkT7E'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return(render_template("index.html"))

@app.route('/telegram', methods=['GET','POST'])
def telegram():
    #grab id
    time.sleep(5) #ensure telegram is activated
    response = requests.get(BASE_URL + 'getUpdates')
    data = response.json()
    text = data['result'][-1]['message']['text']
    chat_id = data['result'][-1]['message']['chat']['id']
    print("Text:", text)
    print("Chat ID:", chat_id)
    send_url = BASE_URL + f'sendMessage?chat_id={chat_id}&text={"Welcome to prediction, please enter the salary"}'
    requests.get(send_url)
    time.sleep(6)
    response = requests.get(BASE_URL + 'getUpdates')
    data = response.json()
    text = data['result'][-1]['message']['text']
    if text.isnumeric():
        msg = str(float(text) * 0.2 + 100)
        send_url = BASE_URL + f'sendMessage?chat_id={chat_id}&text={msg}'
        requests.get(send_url)
    else:
        msg = "salary must be a number"
        send_url = BASE_URL + f'sendMessage?chat_id={chat_id}&text={msg}'
        requests.get(send_url)
        send_url = BASE_URL + f'sendMessage?chat_id={chat_id}&text={"Welcome to prediction, please enter the salary"}'
        requests.get(send_url)
        time.sleep(3)
    return(render_template("index.html"))

if __name__ == '__main__':
    app.run()


