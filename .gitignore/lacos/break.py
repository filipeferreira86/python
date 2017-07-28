print('*'*10, 'Este é o while', '*'*10)
i=0
int(i)
while (i<=2):
    print('Estou pensando em %d'%(i))
    rep = input('Digite S para continuar: ')
    i+=1
    if(rep!='S' and rep!='s'):
        break
else:
    print('Terminei de pensar :)')

print('\n\n', '*'*10, 'Este é o for', '*'*10)

for t in range(0, 10, 2):
    print('agora estou pensando em %d'%(t))
    rep = input('Digite S para continuar: ')
    i += 1
    if (rep != 'S' and rep != 's'):
        break
else:
    print('Terminei aqui também!')