# Retorno mais de um valor

def func():
    return 1, 2

a, b = func()
print(type(a))

def potencia(x):
    quadrado = x**2
    cubo = x**3

    return quadrado, cubo

q, c = potencia(10)

print(q)
print(c)