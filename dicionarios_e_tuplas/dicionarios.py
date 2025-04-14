# dicionários são pares de chave / valor 
# vou ter 1 chave e essa chave corresponde a 1 valor
# a ordem influencia!! Primeiro SEMPRE a chave, depois o VALOR

dados_teo = {"nome":"Téo", "filhos":True, "formacao":["estatística", "BigData DataScience"]}

print(dados_teo)
print(dados_teo["formacao"][-1])

#como adicionar uma nova chave no dicionario
dados_teo["Estado Civil"] = "Casado"

print(dados_teo)

#se eu quiser descobrir as chaves

print("Chaves:", dados_teo.keys())

#se eu quiser saber apenas os valores

print(dados_teo.values())

#comando para imprimir os 2 porém em Tuplas

print("Items:", dados_teo.items())

#usando estrutura de repetição for

for i in dados_teo:
    print(i, "->", dados_teo[i])

print("Outra forma!")

# outra forma de fazer

for chave in dados_teo:
    print(chave, "->", dados_teo[chave])

#também podemos fazer o código assim
#onde chave, valor podem estar ou não entre [], não muda a execução do programa

for chave, valor in dados_teo.items():
    print(chave, "->", valor)