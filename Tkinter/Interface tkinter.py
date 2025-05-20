import tkinter as tk

# Função exibir mensagem ao apertar o botão
def exibir_mensagem():
    print("Você apertou o botão!")

# Criar uma janela
janela = tk.Tk()
janela.title("Primeira Interface Tkinter")

# Adicionar um rótulo
rotulo = tk.Label(janela, text = "Seja bem-vindo")

# Posicionando rotulo na linha 0, coluna 1 e com 20px de distancia no eixo x e no y
rotulo.grid(row=0, column=1, padx=20, pady=20)

# Configura botão, para exibir mensagem
botao = tk.Button(janela, text= "Clique aqui!", command=exibir_mensagem)

# Posicionando botao na linha 1 na coluna 1 e com 20px de distancia no eixo x e 30 no eixo y
botao.grid(row=1, column=1, padx=20, pady=30)

# Executa o loop principal
janela.mainloop()

