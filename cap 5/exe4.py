def recurse(n, s):
    """
    Calcula a soma acumulada de s + n + (n-1) + ... + 1 recursivamente.
    Imprime o resultado quando n atinge 0.

    Parâmetros:
        n (int): Deve ser um número inteiro não-negativo.
        s (int): Valor inicial da soma.

    Exemplo:
        >>> recurse(3, 0)
        6  # (0 + 3 + 2 + 1)
    """
    if n < 0:
        print("Erro: n não pode ser negativo")
        return
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

print("=== Teste 1: recurse(3, 0) ===")
recurse(3, 0)

print("\n=== Teste 2: recurse(-1, 0) ===")
recurse(-1, 0)

print("\n=== Teste 3: recurse(5, 2) ===")
recurse(5, 2)