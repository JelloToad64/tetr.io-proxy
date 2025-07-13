from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/toad64')
def proxy():
    url = 'https://ch.tetr.io/api/users/toad64/summaries'
    headers = {"User-Agent": "Toad64's backend thing (ideally you'd put your email here)"}
    
    headers = {"User-Agent": "Toad64's backend thing (af4toad@gmail.com)"}

    response = requests.get(url, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
