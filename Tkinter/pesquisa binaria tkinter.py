import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Pesquisa binária")

rotulo = tk.Label(janela, text= "MENU PRINCIPAL")
rotulo.grid(row=0, column=1, padx= 100, pady=100)

rotulo_lista = tk.Label(janela, text="Digite uma lista de números separados por espaço:")
rotulo_lista.grid(row=1,column=1, pady= 10)

entry = tk.Entry(janela, width=30)
entry.grid(row=2, column=1, pady=10)

def entrada_lista():
    lista_numeros = entry.get()
    messagebox.showinfo(f"Você digitou: {lista_numeros}")

botao = tk.Button(janela, text="Confirmar", command=entrada_lista)
botao.grid(row=3, column=1, pady=60)

janela.mainloop()

