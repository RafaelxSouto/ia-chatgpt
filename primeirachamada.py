import os
from openai import OpenAI
from dotenv import load_dotenv


#carregar o arquivo {env}
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

resposta = client.chat.completions.create(
    model='gpt-4o-mini',
    max_tokens=500,
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

