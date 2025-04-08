preco_capa = 24.95
desconto = 0.40
quantidade = 60

preco_com_desconto = preco_capa * (1 - desconto)
custo_livros = preco_com_desconto * quantidade

transporte_primeiro = 3.00
transporte_adicional = 0.75
custo_transporte = transporte_primeiro + (quantidade - 1) * transporte_adicional

custo_total = custo_livros + custo_transporte

print(f"Custo total para {quantidade} cópias: R$ {custo_total:.2f}")