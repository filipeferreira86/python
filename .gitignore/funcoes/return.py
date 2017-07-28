# retornando valores qualquer coisa depois do return de uma função ñ executa

def soma(x, y):
    num = x*y
    return num

v1 = int(input('Digite fator 1'))
v2 = int(input('Digite fator 2'))
soma1 = soma(v1,v2)
print(soma1)
