#Exercício 3 — Estatísticas com
#
#Você tem um DataFrame com dados de vendas:
#
#Calcule o total de vendas por produto.
#
#Qual foi o produto com maior valor médio de venda?
#
#Adicione uma coluna com o valor acumulado (cumulativo) por linha.

# %%
import pandas as pd

dados = {
    'produto': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'valor': [100, 200, 150, 300, 250, 120, 280]
}

df = pd.DataFrame(dados)

# 1. Total de vendas por produto
total_vendas = df.groupby('produto')['valor'].sum()
print("\n🔹 Total de vendas por produto:")
print(total_vendas.to_string())  # Melhor formatação

# 2. Produto com maior valor médio
media_vendas = df.groupby('produto')['valor'].mean()
produto_maior_media = media_vendas.idxmax()
print(f"\n🔹 Produto com maior valor médio: '{produto_maior_media}' (Média = {media_vendas.max():.2f})")

# 3. Valor acumulado
df['valor_acumulado'] = df['valor'].cumsum()
print("\n🔹 DataFrame com valor acumulado:")
print(df)
# %%
