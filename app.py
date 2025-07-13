from flask import Flask, jsonify
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return '''
        <html>
            <head><title>Toad64 Proxy</title></head>
            <body style="text-align: center; margin-top: 50px;">
                <h1>Welcome to the Toad64 tetr.io Proxy</h1>
                <img src="/static/goofy.jpg" alt="Goofy Image" width="400">
                <p>Try <a href="/toad64">/toad64</a> for the real deal</p>
            </body>
        </html>
    '''

@app.route('/toad64')
def proxy():
    url = 'https://ch.tetr.io/api/users/toad64/summaries'
    
    headers = {"User-Agent": "Toad64's backend thing (af4toad@gmail.com)"}

    response = requests.get(url, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
