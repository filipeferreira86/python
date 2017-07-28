#Para adiconar um novo item a lista deve-se informar o nome da lista
#recebendo o nome da lista novamente + para concatenar e a nova lista []

lista = [10, 11, 12, 13]
lista = lista+[2]

print(lista)

novonum = int(input("Novo item a lista"))
lista = lista + [novonum]

print(lista)

print('*'*10, 'Novo item', '*'*10)
print('Excluindo item 0')
del(lista[0])
print('Item 0 excluido')
print(lista)