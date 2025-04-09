def do_twice(f, valor):
    f(valor)
    f(valor)
    
def do_four(f, valor):
    do_twice(f, valor)
    do_twice(f,valor)

def print_oi(mensagem):
    print(mensagem)

do_four(print_oi, "Olá, Mundo!" )