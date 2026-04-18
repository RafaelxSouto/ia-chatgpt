from dotenv import load_dotenv
import os

load_dotenv()
chave = os.getenv('OPENAI_API_KEY')
print(chave)
