import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Pesquisa binária")

# ----- FUNÇÃO DA PESQUISA BINÁRIA --------
def pesquisa_binaria(lista, numero_procurado): 
    baixo = 0 
    alto = len(lista) - 1 

    while baixo <= alto: 
        meio = (baixo + alto) // 2 
        valor_meio = lista[meio] 
            
        if valor_meio == numero_procurado:
            return meio 
        elif valor_meio > numero_procurado: 
            alto = meio - 1 
        else: 
            baixo = meio + 1 
    return None 

# -------- FUNÇÃO CHAMADA DEPOIS QUE LISTA É INSERIDA --------
def processar_lista(entry):
    entrada = entry.get()
    try:
        lista_numeros = [int(n) for n in entrada.strip().split()]
        lista_numeros.sort()
        messagebox.showinfo("Lista processada", f"Sua lista ordenada é: {lista_numeros}")
        buscar_numero(lista_numeros)  # Avança para a próxima etapa
    except ValueError:
        messagebox.showerror("Erro!", "Digite apenas números separados por espaços.")

# -------- FUNÇÃO QUE PROCURA NÚMERO NA LISTA ----------
def ao_confirmar_busca(entry, lista_numeros):
    entrada = entry.get().strip()

    if entrada.upper() == "SAIR":
        messagebox.showinfo("Encerrando", "Encerrando sua busca...")
        janela.quit()
    else:
        try:
            numero = int(entrada)
            resultado_posicao = pesquisa_binaria(lista_numeros, numero)

            if resultado_posicao is not None:
                messagebox.showinfo("Resultado", f"O número está na posição {resultado_posicao}")
            else:
                messagebox.showwarning("Não encontrado", "Número não está na lista.")
        except ValueError:
            messagebox.showerror("Erro!", "Digite um número inteiro válido ou 'SAIR'.")

# -------- TELA PARA DIGITAR A LISTA --------
def menu_inicial():
    limpar_janela()
    tk.Label(janela, text="MENU INICIAL").grid(row=0, column=1, padx=100, pady=10)
    tk.Label(janela, text="Digite uma lista de números, separando por espaços:").grid(row=1, column=1, pady=10)

    entry = tk.Entry(janela, width=30)
    entry.grid(row=2, column=1, pady=10)

    botao = tk.Button(janela, text="Confirmar", command=lambda: processar_lista(entry))
    botao.grid(row=3, column=1, pady=60)

# -------- TELA PARA BUSCAR NÚMERO --------
def buscar_numero(lista_numeros):
    limpar_janela()
    tk.Label(janela, text="Digite o número que deseja procurar: (ou digite SAIR)").grid(row=1, column=1, pady=10)

    entry = tk.Entry(janela, width=30)
    entry.grid(row=2, column=1, pady=10)

    botao = tk.Button(janela, text="Buscar", command=lambda: ao_confirmar_busca(entry, lista_numeros))
    botao.grid(row=3, column=1, pady=60)

# -------- LIMPAR JANELA --------
def limpar_janela():
    for widget in janela.winfo_children():
        widget.destroy()

# -------- INICIAR PROGRAMA --------
menu_inicial()
janela.mainloop()
