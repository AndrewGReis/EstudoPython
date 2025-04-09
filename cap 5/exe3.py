def verifica_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Sim, pode formar um triângulo!")
    else:
        print("Não, não pode formar um triângulo")

print("Digite três comprimentos de gravetos:")
a = int(input("Grave 1: "))
b = int(input("Grave 2: "))
c = int(input("Grave 3: "))

verifica_triangulo(a, b, c)