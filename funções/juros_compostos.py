# %%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """isto é chamado de doc string
conseguimos escrever uma documentação durante o código
aporte:
    um número inteiro, que represente o valor em R$
taxa:
    um número float entre 0 e 1 que represente o valor taxa de juros
anos:
    um número inteiro >= 1 que represente o tempo de investimento terá liquidez
    """
    return aporte * (1 + taxa) ** anos


# %%
juros_compostos(aporte = 1000, taxa = 0.13, anos = 4)
# %%
