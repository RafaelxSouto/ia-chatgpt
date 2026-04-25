from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return jsonify({'mensagem': 'Olá! Meu servidor está funcionando!'})

@app.route('/sobre')
def sobre():
    return 'Esta é a página sobre!'

@app.route('/chat', methods=['POST'])
def chat():
    dados = request.get_json()

    if not dados:
        return jsonify({'erro': 'Nenhum dado recebido'}), 400

    mensagem = dados.get('mensagem', '')

    if not mensagem:
        return jsonify({'erro': 'Mensagem vazia'}), 400

    return jsonify({'resposta': 'Você disse: ' + mensagem, 'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)