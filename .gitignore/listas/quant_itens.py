lista = ['Filipe', 'Josué', 'Aline', 'Marcos', 'Terilo', 'Terencio', 'Maria']
print(lista)
print('Tamanho da lista e seu ultimo item')
print(len(lista))
print(lista[len(lista)-1])

print('*'*20, 'Para contar elementos repetidos', '*'*20)
lista.insert(4, 'Josué')
lista.append('Josué')

print('Foi incluido novamente josué na lista 2 vezes totalizando 3 vezes o mesmo conteudo')
print(lista)
print('Estou contando a quantidade de vezes Josué aparece')
print(lista.count('Josué'))

print('*'*20, 'Para mostrar o indice da um item', '*'*20)
print('Neste caso quero o indice de Filipe')
print(lista.index('Filipe'))

print('Agora quero o indice de Josué')
print(lista.index('Josué'))
print('ele mostra somente a primeira ocorrencia, lê e sai')

