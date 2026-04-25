#Código que cria um servidor web simples
from flask import Flask

app = Flask(__name__)       #Cria a aplicação Flask

@app.route("/")             #Define a rota para a página inicial
def pagina_inicial():
    return "Olá! Meu servidor está funcionando!"   #Retorna uma mensagem para a página inicial

@app.route("/sobre")        #Define a rota para a página "sobre"
def sobre():
    return "Esta é a página sobre!"

# Inicia o servidor web
if __name__ == "__main__":
    app.run(debug=True)     #Inicia o servidor em modo de depuração

#  para acessar o servidor, abra um navegador e vá para http://localhost:5000/ para a página inicial e http://localhost:5000/sobre para a página "sobre".
