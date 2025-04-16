#Exercício 1 — Análise de Array NumPy
#
#Você recebeu um array NumPy com os valores de temperatura (em °C) registrados ao longo de uma semana:
#
#
#
#1.   Calcule a temperatura média da semana.
#2.   Encontre a temperatura mais alta e a mais baixa.
#3.   Quantos dias ficaram acima da média?

# %%
import pandas as pd
# %%
temperaturas = [22.5, 23.0, 19.5, 21.0, 25.2, 26.3, 24.5]

media = sum(temperaturas) / len(temperaturas)

temp_maxima = max(temperaturas)
temp_minima = min(temperaturas)

dias_acima_media = sum(1 for temp in temperaturas if temp > media)

print(f"Temperatura Máxima: {temp_maxima:.2f}")
print(f"Temperatura Mínima: {temp_minima:.2f}")
print(f"A média das temperaturas é: {media:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")
# %%
