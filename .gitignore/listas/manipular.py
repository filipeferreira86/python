lista = ['b', 'c', 'd', 'e', 'f', 'g', 'h']

print('*'*20, 'inclusão no fim', '*'*20)
lista.append('i')
print('Incluido i no fim')
print(lista)
print('*'*20, 'inclusão na posição desejada', '*'*20)
lista.insert(0,'a')
print('Incluido a no inicio')
print(lista)

print('*'*20, 'alterar elemento', '*'*20)
lista[1] = 'bb'
print('alterado indice 1')
print(lista)

print('*'*20, 'Excluindo ultimo item', '*'*20)
lista.pop()
print('ultimo item excluido')
print(lista)

print('*'*20, 'Excluindo qq item', '*'*20)
lista.pop(0)
print('primeiro item excluido')
print(lista)

print('*'*20, 'Excluindo varios itens', '*'*20)
del(lista[0:2:1])
print('3 itens excluidos')
print(lista)

print('*'*20, 'Excluindo varios itens com passada', '*'*20)
del(lista[0:2:2])
print('3 itens excluidos')
print(lista)

print('*'*20, 'Limpando lista', '*'*20)
lista.clear()
print('Lista limpa')
print(lista)