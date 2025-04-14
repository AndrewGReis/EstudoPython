# Escreva um programa que crie um dicionário com nomes de frutas como chaves e seus respectivos preços como valores.
# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.
# posso fazer com if elif e else porém não fica bom, resolve mas não da melhor forma

fruta = input("Entre com o nome da fruta:")

frutas = {
    "Maçã": "R$1,50", 
    "Pera": "R$1,25", 
    "Goiaba": "R$2,15", 
    "Banana": "R$2,75",
    "Laranja": "R$0,65", 
    "Abacaxi": "R$3,20", 
    "Uva": "R$1,90", 
    "Limão": "R$1,25", 
    "Jaca": "R$5,80"
           }

if fruta in frutas:
     print(frutas[fruta])
else:
     print("Entre com uma fruta do cardápio")
