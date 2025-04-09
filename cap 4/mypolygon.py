import turtle

def square(t):
    for _ in range(4):
        t.fd(100)
        t.lt(90)

bob = turtle.Turtle()
square(bob)

turtle.done()