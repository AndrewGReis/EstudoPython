# Faça um programa que receba um número.
#Verifique se o número informado é par ou ímpar.
#Exiba o resultado da seguinte maneira:
#
#O número x é par 
#ou
#O número x é ímpar



def par_impar(numero:int):
    if numero % 2 == 0:
        print("O número", numero, "é par.")
    else:
        print("O número", numero, "é ímpar.")

numero = input("Informe um número: ")
numero = int(numero)

par_impar(numero)