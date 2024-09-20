#Calculadora em python
import os
os.system("cls")

#Acrescentando as funções com parâmetro
def somar (numero1,numero2):       #Função para a soma de dois números.
    return numero1+numero2

def subtrair (numero1,numero2):    #Função para a subtração de dois números.
    return numero1-numero2

def multiplicar (numero1,numero2): #Função para a multiplicação de dois números.
    return numero1*numero2

def divisao (numero1,numero2):     #Função para a divisão de dois números.
    return numero1/numero2

opcao_menu = {
    1: "-----MENU----- \n1 - Adição",
    2: "1 - Subtração",
    3: "1 - Multiplicação",
    4: "1 - Divisão",
}


for chave, valor in opcao_menu.items():
    print(valor)


opcao_usuario = int (input("\nDigite o número da opção desejada:"))





