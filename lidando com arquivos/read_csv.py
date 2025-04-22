# %%

arquivo = "praticando_data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()

for l in lines:
    print(l)
# %%

dados = dict()

chaves = lines[0].strip("\n").split(";")
for c in chaves:
    dados[c] = []

dados

# %%

for l in lines[1:]:
    valores = l.strip("\n").split(";")
    # i é o índice
    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i])

dados

# %%

idades = []
for i in dados["idade"]:
    idades.append(int(i))

idades
# %%

media = sum(idades) / len(idades)
print(media)
# %%
