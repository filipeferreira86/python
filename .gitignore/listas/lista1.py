#Listas 1
lista = [1, 2, 3, 5, 7, 10, 3.4]
print(lista)
print(type(lista))
num = int(input('Digite o numero da lista: '))
print(lista[num])

#Outro jeito
lis1 = list(('Filipe Ferreira de Jesus', 'ola', 88))
print(lis1)

#Para declarar ua lista com parenteses é necessário informar uma virgula no final

lis2 = list('ola',)
print(type(lis2))

#ver tamanho lista de lista

print(len(lis2))
print(len(lis1))
lis3 = [[10, 15,8], [3, 5, 6], 2]
print(lis3[1][0])