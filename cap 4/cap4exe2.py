import turtle

bob = turtle.Turtle()
bob.speed(5)
bob.pensize(2)


def desenhar_fatia(t, raio, angulo):
    t.fd(raio)
    t.lt(90)
    t.circle(raio, angulo)
    t.lt(90)
    t.fd(raio)
    t.lt(180 - angulo)


for _ in range(4):
    desenhar_fatia(bob, 100, 90)

turtle.done()