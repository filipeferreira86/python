lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('*'*20, 'Lista antes da manipulção', '*'*20)
print(lista)

print('*'*20, 'Invertendo a lista', '*'*20)
#Ele não executa a inversão fisicamente somente diz q a lista deve ser lida inversamente
lista.reverse()
print(lista)
print('indice 1 é: ', lista[1])

print('*'*20, 'Ordenando na ordem ascendente(menor pro maior)', '*'*20)
lista.sort()
print(lista)
print('indice 1 é: ', lista[1])

print('*'*20, 'Ordenando na ordem descendente(maior pro menor)', '*'*20)
lista.sort(reverse=True)
print(lista)
print('indice 1 é: ', lista[1])