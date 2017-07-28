# Parametros em funções

print()

def soma(x,y):
    print('*'*10, 'SOMA', '*'*10)
    sum=x+y
    print('O total da some de {} + {} é: {}'.format(x, y, sum))

val1 = int(input('digite o primeiro valor'))
val2 = int(input('digite o segundo valor'))

soma(val1, val2)