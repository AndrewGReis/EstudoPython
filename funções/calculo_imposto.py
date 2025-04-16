# %%
def calc_imposto(preco:float, tx_base:float, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto

# %%
calc_imposto(100, 0.03, municipio=0.01, estadual=0.002, nacional=0.001)

# também posso fazer assim:
#impostos_gerais= {
#    "municipio"=0.01, 
#    "estadual"=0.002, 
#    "nacional"=0.001
#    }
#aí posso ler assim
#calc_imposto(100, 0.03, **impostos_gerais)