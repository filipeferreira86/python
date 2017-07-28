#Iterando strings

print('*'*10,'Exemplo 1', '*'*10)
s = 'iterando strings'
for c in s:
    print(c)

#2

print('*'*10, 'Exemplo 2', '*'*10)

indice1 = 0
while indice1<len(s):
    print(indice1, '-', s[indice1])
    indice1 += 1

print('*'*10,'Exemplo 3', '*'*10)

#enumerate vincuala cada objeto a um numero iniciando em 0 ele vai usar sempre uma chave e um valor, nesta ordem, dessa forma a primeira ação será 0 = i,

for k, v in enumerate(s):
    print(k, '-', v)