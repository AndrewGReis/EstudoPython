teo = ["Téo Calvo", 32, True, "Casado",["estagiário", "ds.Jr.", "ds.Pleno", "ds.Senior", "Head"],
 [1500, 4000, 4550, 6500, 10000],["Ana", "Maria", "Cláudia"]]
exs = teo[-1]
primeira_ex = exs[0]

print(len(teo))
print(teo[-1][1])

print(primeira_ex)

# caso eu queira acessar a última posição da tabela

tamanho = len(teo)
pos = tamanho -1
teo[pos][1]

#fatiamento de listas

#vamos supor que eu quero a lista teo e os 3 primeiros elementos

teo[0:4]
# precisa ser 0:4 pq ele faz a conta 4 - 0, ou seja, puxa 4 elementos de intervalo aberto


# quero saber quais foram as duas ultimas posições de mercado do teo

# para lembrar a listateo = ["Téo Calvo", 32, True, "Casado",["estagiário", "ds.Jr.", "ds.Pleno", "ds.Senior", "Head"], [1500, 4000, 4550, 6500, 10000],["Ana", "Maria", "Cláudia"]]

ultimas_posic = teo[4][3:5]
ultimas =teo[4][-2:]
# ao usarmos [-2:] estamos dizendo que queremos o penúltimo elemento até o final da lista
# podemos considerar [ start : stop]
# onde start seria considerar o primeiro ítem de início da lista e stop considerar o último item, o final da lista
# foca assim para fazer o fatiamento [ start : stop : step]
#                  ou seja [ aonde eu começo : aonde é o meio : aonde é o fim]
salarios = teo[5]

print(ultimas_posic)
print(ultimas)
print(teo[1 : 4])
print(salarios)
print("De 1 em 1 do começo até o final", (salarios[::]))
print("De 1 em 1 do final até o começo",salarios[::-1])
