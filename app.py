# app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/toad64')
def proxy():
    res = requests.get('https://ch.tetr.io/api/users/toad64')
    return jsonify(res.json())

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
