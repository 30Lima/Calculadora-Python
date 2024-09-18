#Calculadora em python

import os

os.system("cls")

#Acrescentando as funções com parâmetro

def somar (numero1,numero2):
    return numero1+numero2

op_usuario = int(input("------MENU-----\n"
                         "1 - Adição\n"
                         "2 - Subtração\n"
                         "3 - Multiplicação\n"
                         "4 - Divisão\n"
                         "--------------------\n"
                        "Digite o número da opção desejada: "))


