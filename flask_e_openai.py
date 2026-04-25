# Esse código recebe mensagem, acessa a API da OpenAI e devolve uma resposta

from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = '''
Você é um assistente de programação didático.
Explique conceitos de forma simples, com exemplos.
Use linguagem acessível para iniciantes.
'''


@app.route('/')                     # serve a página HTML
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    dados = request.get_json()
    historico = dados.get('historico', [])  # historico vem do frontend
    mensagem = dados.get('mensagem', '')

    # Monta mensagens: system + historico + nova mensagem
    mensagens = [{'role': 'system', 'content': SYSTEM_PROMPT}]
    mensagens += historico
    mensagens.append({'role': 'user', 'content': mensagem})

    try:
        resp = client.chat.completions.create(
            model='openai/gpt-oss-20b',
            messages=mensagens,
            max_tokens=1000
        )
        texto = resp.choices[0].message.content
        return jsonify({'resposta': texto})

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
