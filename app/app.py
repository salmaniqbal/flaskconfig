from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import configparser

app = Flask(__name__)

with open('config.json', 'r') as f:
    config = json.load(f)

def favorite_colors() -> List[Dict]:
    user = config['DEFAULT']['USER']
    password = config['DEFAULT']['PASSWORD']
    host = config['DEFAULT']['HOST']
    port = config['DEFAULT']['PORT']
    database = config['DEFAULT']['DATABASE']

    dbconfig = {
        'user': user,
        'password': password,
        'host': host,
        'port': port,
        'database': database
    }
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results

@app.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})

@app.route('/test')
def index2() -> str:
    secret_key = config['DEFAULT']['USER']
    return secret_key

if __name__ == '__main__':
    app.run(host='0.0.0.0')