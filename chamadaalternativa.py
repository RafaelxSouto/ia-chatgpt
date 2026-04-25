import os
from groq import Groq
from dotenv import load_dotenv


#carregar o arquivo {env}
load_dotenv()
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

resposta = client.chat.completions.create(
    model='openai/gpt-oss-120b',
    max_tokens=2000,
    temperature=0.7,        #criatividade: 0=preciso, 2=criativo
    messages=[
        {
            'role': 'system',
            'content': 'Você é um assitente educacional'
        },
        {
            'role': 'user',
            'content': 'O que é Python em uma frase?'
        }
    ]

)

# Acessando a resposta
texto = resposta.choices[0].message.content
print(texto)

# Verificando o uso de tokens
print(f'Tokens usados: {resposta.usage}')

