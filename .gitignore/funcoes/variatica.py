# Funções variáticas são as que podem receber uma quantidade n de parametros
# Quando quiser receber uma quantidade maior de parametros deve ser iniciado com * desta forma receberá uma lista

def lista_de_arg(*lista):
    print(lista)

# Quando quiser receber um dicionário ou seja incluindo o nome

def associativos(**dicionario):
    print(dicionario)

def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)

lista_de_arg(1, 2, 3, 4, 5, 6, 7, 8, 9)
lista_de_arg('um', 'dois', 'tres')

associativos(a=1, b=2, c=3)

argumentos(1, 2, 'bb', tres=3, dois=2, um=1)