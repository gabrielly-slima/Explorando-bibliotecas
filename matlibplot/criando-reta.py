import matplotlib.pyplot as plt

def pedir_valores(eixo):
    '''
    Solicita ao usuário duas coordenadas para o eixo especificado (X ou Y).

    Parâmetros:
    eixo (str): Nome do eixo a ser exibido na mensagem (ex: 'X' ou 'Y').

    Retorna:
    list[float]: Lista com duas coordenadas convertidas para float.
    '''
    while True:
        valores = input(f"Digite duas coordenadas do eixo {eixo} separando-as por espaços\n").split()
        if len(valores) > 2:
            print("Você digitou coordenadas a mais, digite apenas DUAS")
            continue
        elif len(valores) > 1:
            try:
                converter_coordenadas = [float(num) for num in valores]
                return converter_coordenadas
            except ValueError:
                print(f"As coordenadas de {eixo} devem ser números válidos")
        else:
            print("Digite mais uma coordenada")

def mostrar_valores(coordenadas_x,coordenadas_y):
    '''
    Exibe as coordenadas inseridas pelo usuário.

    Parâmetros:
    coordenadas_x (list[float]): Coordenadas do eixo X.
    coordenadas_y (list[float]): Coordenadas do eixo Y.
    '''
    print(f"Sua reta será composta das seguintes coordenadas: X(a,b) = {coordenadas_x[0]},{coordenadas_x[1]} Y(a,b) = {coordenadas_y[0]},{coordenadas_y[1]}")

def criar_reta(coordenadas_x,coordenadas_y):
   '''
    Cria e exibe um gráfico com uma reta entre os dois pontos fornecidos.

    Parâmetros:
    coordenadas_x (list[float]): Coordenadas do eixo X.
    coordenadas_y (list[float]): Coordenadas do eixo Y.
    '''
   x = coordenadas_x
   y = coordenadas_y

   plt.plot(x,y)
   plt.xlabel("Eixo X")
   plt.ylabel("Eixo Y")
   plt.title("Criando uma Reta")
   plt.show()

def main():
    '''
    Função principal que executa o menu de criação de retas.

    O usuário escolhe entre criar uma reta ou encerrar o programa.
    '''
    while True:
        entrada = input("CRIANDO UMA RETA\nDigite:\n1 para CRIAR UMA RETA ou 0 para SAIR\n")
        if entrada == "1":
            try:
                coordenadas_x = pedir_valores("X")
                coordenadas_y = pedir_valores("Y")
                mostrar_valores(coordenadas_x,coordenadas_y)
                criar_reta(coordenadas_x,coordenadas_y)
            except ValueError:
                print("Digite um caractere válido")
        elif entrada =="0":
            print("Encerrando...")
            break
        else:
            print("Digite um caractere válido\n")
            continue
    
main()