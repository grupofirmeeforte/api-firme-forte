from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "API Firme Forte no ar!", "ok": True})

@app.route('/teste')
def teste():
    return jsonify({"mensagem": "Deploy funcionou!"})

if __name__ == '__main__':
    app.run()
