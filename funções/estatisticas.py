def soma(a:float, b:float)->float:
    return a + b

def media(a:float, b:float)->float:
    return soma(a,b) / 2

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))

print("Média: ", media(a, b))