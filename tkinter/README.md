# Tkinter - Biblioteca GUI do Python
Tkinter é a biblioteca padrão do Python para criação de interfaces gráficas (GUI - Graphical User Interface). Ela permite criar janelas, botões, caixas de texto e outras interações visuais, tudo de forma simples e integrada ao Python.
Facilita a criação de aplicativos gráficos, desde janelas simples até interfaces complexas.
Está incluído na instalação padrão do Python, sem necessidade de instalar pacotes extras.
Muito usada para prototipagem rápida e aplicações desktop simples.

## Funções e componentes Tkinter que mais utilizo:

Componente|Função/Descrição|Exemplo no código
---|---|---
tk.Tk()|Cria a janela principal da aplicação GUI|janela = tk.Tk()
window.title("texto")|Define o título da janela principal|janela.title("Pesquisa binária")
tk.Label()|Cria um texto fixo na janela (rótulo)|tk.Label(janela, text="MENU INICIAL").grid(...)
tk.Entry()|Campo de entrada para o usuário digitar texto/números|entry = tk.Entry(janela, width=30)
tk.Button()|Botão clicável que executa uma função ao ser pressionado|tk.Button(janela, text="Confirmar", command=...)
widget.grid()|Organiza o widget em uma grade (linha x coluna)|Usado para posicionar Labels, Entrys e Buttons.
widget.destroy()|Remove um widget da janela, usado para limpar a interface|limpar_janela() usa isso para limpar tudo.
messagebox.showinfo()|Exibe uma caixa de diálogo informativa (botão OK)|messagebox.showinfo("Título", "Mensagem")
messagebox.showerror()|Exibe uma caixa de diálogo de erro\messagebox.showerror("Erro!", "Mensagem")
messagebox.showwarning()|Exibe um alerta de aviso|messagebox.showwarning("Não encontrado", ...)
mainloop()|Inicia o loop principal que mantém a janela aberta|janela.mainloop()

### Como o programa funciona com Tkinter (Pesquisa Binária)
**Janela principal criada:**
janela = tk.Tk() inicia a janela da aplicação.

**Entrada da lista:**
Usuário digita números separados por espaços em um campo Entry.

**Botão "Confirmar":**
Quando clicado, processa a lista (ordena e valida os números).

**Mensagem informativa:**
Mostra lista ordenada usando messagebox.showinfo.

**Busca binária:**
Solicita número a procurar e informa o resultado (posição ou alerta se não encontrado).

**Limpeza da tela:**
A função limpar_janela() remove todos os widgets para trocar a interface.

**Controle de fluxo:**
O programa usa funções encadeadas para mudar entre telas de entrada e busca.