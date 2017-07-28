# funções
# Dicionario de telefone
tel = {
    967303221: 'Filipe',
    952604917: 'Outro'
}
print(tel)
print('este dicionario possui {} numeros'.format(len(tel)))
print('Deletar 1 numero')
del (tel[952604917])
print(tel)
print('chaves:')
print(tel.keys())
print('valores: ')
print(tel.values())

print('Novo dic')
tel2 = {
    987303221: 'Filipe',
    992604917: 'Outro',
    992604918: 'Outro2',
    992604919: 'Outro3'
}
print(tel2)
# para retornar um elemento e remove-lo do dic basta usar a função popitem
print(tel2.popitem())
print(tel2)

#unir diconarios:
tel.update(tel2)
print(tel)