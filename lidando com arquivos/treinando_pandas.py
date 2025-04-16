#Utilizando a biblioteca Pandas
#usar o comando pip install pandas no terminal 
#%%
import pandas as pd
#Biblioteca Numpy
import numpy as np
#Biblioteca de gráficos Matplotlib
# instalação a partir de pip install matplotlib
# %%
import matplotlib.pyplot as plt
# %%
temperaturas = pd.Series([20,25,30,35,40])

print(temperaturas)
# %%
temperaturas

# %%
temperaturas.values

# %% 
temperaturas.index
# %%
# acrescentando mais informações
temperaturas = pd.Series([20, 22, 25, 35, 32, 40, 100],
                          index=["Itatiaia", "Petrópolis", "Teresópolis", "Niterói", "Friburgo", "Rio de Janeiro", "Bangu"])

temperaturas
print(temperaturas.sort_values(ascending=True))

# %%
# verificando temperatura de uma cidade em específico
print(temperaturas['Petrópolis'])
# %%
# por já termos importado as bibliotecas nao precisamos definir 
# algumas funções como por exemplo média de temperatura
print("Média:", temperaturas.mean())

# %%
# essa seria uma possível função para calcular a média manualmente
def media_manual(lista):
    soma = sum(lista)
    quantidade = len(lista)
    media = soma / quantidade
    return media

print("Média: ", media_manual(temperaturas))
# %%
# outra função, verificando mediana agora
print("A mediana das temperaturas é:", temperaturas.median())
# construindo um data frame para testar
# %%
df = pd.DataFrame({'municipio' : ["Petrópolis", "Itatiaia", "Teresópolis", "Niterói", "Rio de Janeiro"],
                   'populacao' : [306678,29996,185820,513584,6775561],
                   'clima' : ['tropical de altitude','subtropical','oceânico de altitude','tropical','tropical atlântico'],
                   'altitude': [838,1648,869,2,2],
                   'area': [795798,224957,770000,129.3,1200329],
                   'idh': [0.745,0.737,0.730,0.837,0.799]})

# %%
df.dtypes
# %%
df.columns
# %%
df['municipio']
# Ordenando por uma coluna em específico
# %%
df.sort_values(by = "municipio")
# pegando valores estatísticos por exemplo
# %%
df.describe()
# consultando uma condição simples
# %%
df[df["altitude"] > 500]
# consultando uma condição composta
# %%
df[(df["altitude"] > 500) & (df['idh'] > 0.7)]
# %%
