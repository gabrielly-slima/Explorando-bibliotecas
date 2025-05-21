import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Pesquisa binária")

rotulo = tk.Label(janela, text= "MENU PRINCIPAL")
rotulo.grid(row=0, column=1, padx= 100, pady=100)

def pesquisa_binaria(lista, numero_procurado): 
    baixo = 0 
    alto = len(lista) - 1 

    while baixo <= alto: 
        meio = (baixo + alto)//2 
        valor_meio = lista[meio] 
            
        if valor_meio == numero_procurado:
            return meio 
        elif valor_meio > numero_procurado: 
            alto = meio - 1 
        else: 
            baixo = meio + 1 
    return None 

def buscar_numero(lista_numeros):
    rotulo_buscar_numero = tk.Label(janela, text ="Digite o número que deseja procurar: \n Para sair digite SAIR\n")
    rotulo_buscar_numero.grid(row=1,column=1,pady=10)

    entry = tk.Entry(janela, width=30)
    entry.grid(row=2, column=1, pady=10)

    def ao_confirmar():
        entrada = entry.get()
        if entrada.upper().strip() == "SAIR":
            messagebox.showinfo(f"Encerrando sua busca...")
            return
        
        try: 
            numero = int(entrada)
            resultado_posicao = pesquisa_binaria(lista_numeros, numero)

            if resultado_posicao is not None:
                messagebox.showinfo(f"O número está na posição {resultado_posicao}")
            else:
                messagebox.showerror(f"Número não encontrado... Digite um número presente na lista!\n")
            




    botao = tk.Button(janela, text="Confirmar", command=ao_confirmar)
    botao.grid(row=3, column=1, pady=60)
    
