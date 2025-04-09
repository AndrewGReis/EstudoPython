def check_fermat(a, b, c, n):
    """Verifica o Último Teorema de Fermat."""
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def input_and_check_fermat():
    """Pede inputs do usuário e testa o teorema."""
    print("Verifique o Último Teorema de Fermat (a^n + b^n = c^n)")
    
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    n = int(input("Digite o valor de n (deve ser > 2): "))
    
    if n <= 2:
        print("Erro: n deve ser maior que 2 para o teorema!")
    else:
        check_fermat(a, b, c, n)

input_and_check_fermat()