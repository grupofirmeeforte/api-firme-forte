from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "API Firme Forte Online 💚"})

@app.route('/teste')
def teste():
    return jsonify({"mensagem": "Deploy funcionando!"})

# ESTA É A ROTA QUE O LOVABLE CHAMA
@app.route('/criar-checkout', methods=['POST'])
def criar_checkout():
    dados = request.get_json()
    plano = dados.get("plano", "basico")
    
    # LINK FAKE SÓ PRA TESTAR A CONEXÃO
    link_fake = "https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=TESTE123"
    
    return jsonify({
        "url_checkout": link_fake,
        "plano_escolhido": plano
    })

if __name__ == '__main__':
    app.run()
