# Código que cria um chatbot simples em Python

import tkinter as tk #Biblioteca que constroi interface gráfica
import random #Biblioteca de aleatóriedade.

# Respostas simples

respostas = {
    "oi": [
        "Olá!", "Oi! Tudo Bem?", "E aí!"
    ],
    "Tudo bem": ["Tudo ótimo!", "Sim, e vocẽ", "Indo bem"],
    "python": ["Python é ótimo para IA!", "Você está estudando Python?"],
    "ia": ["IA é fascinante!", "Inteligencia Artificial está em todo lugar!"]
}
