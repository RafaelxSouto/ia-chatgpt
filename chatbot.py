# Código que cria um chatbot simples em Python

import tkinter as tk  # Biblioteca que constroi interface gráfica
import random  # Biblioteca de aleatóriedade.

# Respostas simples

respostas = {
    "oi": ["Olá!", "Oi! Tudo Bem?", "E aí!"],
    "tudo bem": ["Tudo ótimo!", "Sim, e vocẽ", "Indo bem"],
    "python": ["Python é ótimo para IA!", "Você está estudando Python?"],
    "ia": ["IA é fascinante!", "Inteligencia Artificial está em todo lugar!"],
}


def responder(msg):
    msg = msg.lower()
    for chave in respostas:
        if chave in msg:
            return random.choice(respostas[chave])
    return "Não entendi, pode reformular?"


def enviar():
    msg = entrada.get()

    if msg.strip() == "":
        return

    chat.insert(tk.END, "Voçê: " + msg + "\n")

    resposta = responder(msg)
    chat.insert(tk.END, "Bot: " + resposta + "\n\n")

    entrada.delete(0, tk.END)


# Interface
janela = tk.Tk()
janela.title("Chatbot IA - Simples")

chat = tk.Text(janela, height=50, width=90)
chat.pack()

entrada = tk.Entry(janela, width=40)
entrada.pack(side=tk.LEFT, padx=5, pady=5)

botao = tk.Button(janela, text="Enviar", command=enviar)
botao.pack(side=tk.LEFT)
chat.configure(font=("Arial", 44))
entrada.configure(font=("Arial", 44))
botao.configure(font=("Arial", 44))

# Tema escuro com texto verde
janela.configure(bg="#121212")

chat.configure(bg="#0d0d0d", fg="#00ff66", insertbackground="#00ff66")

entrada.configure(bg="#1a1a1a", fg="#00ff66", insertbackground="#00ff66")

botao.configure(
    bg="#262626",
    fg="#00ff66",
    activebackground="#333333",
    activeforeground="#00ff66",
    relief=tk.FLAT,
)

janela.mainloop()
