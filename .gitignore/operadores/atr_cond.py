#atribuição condicional

nome = input('Nome')
oi = 'Ola Filipe' if (nome=='Filipe') else'Oi {}'.format(nome)
print (oi)

def numero():
    num1 = input('Digite um numero')
    if(num1.isnumeric()):
        num1 = int(num1)
        s = 'par' if num1%2 == 0 else 'impar'
        print('O número digitado é {}'.format(s))
    else:
        print('Eu disse numero')
        numero()
numero()