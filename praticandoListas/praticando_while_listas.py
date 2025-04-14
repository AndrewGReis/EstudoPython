idades =[]

while True:
  idade = input("Entre com a idade: ")

  if idade == "":
    break

  idades.append(int(idade))

media = sum(idades) / len(idades)

print(idades)
print(media)