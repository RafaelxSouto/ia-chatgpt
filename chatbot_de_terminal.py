import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = "Você é um assistente de programação educacional."

# O histórico começa só com o system prompt
historico = [{"role": "system", "content": SYSTEM_PROMPT}]

print('Chatbot iniciado! Digite "sair" para encerrar.\n')

while True:  # loop infinito
    entrada = input("Você: ").strip()  # lê a mensagem do usuário

    if entrada.lower() == "sair":
        print("Encerrando. Até logo!")
        break

    if not entrada:  # ignora mensagem vazia
        continue

    # Adiciona mensagem do usuário ao histórico
    historico.append({"role": "user", "content": entrada})

    try:
        resposta = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=historico,  # Envia todo o histórico
            max_tokens=800,
        )
        texto = resposta.choices[0].message.content

        # Adiciona resposta da IA ao histórico também
        historico.append({"role": "assistant", "content": texto})

        print(f"\nAssistente: {texto}\n")

    except Exception as e:
        print(f"Erro ao contactar a API: {e}")
