#finaliza o ciclo e reinicia do proximo ponto
num = int(input('Digite o numero para pular'))
for i in range(1,11,1):
    if(i==num):
        continue
    print(i)
else:
    print('escrevi de 1 a 10 pulando %d'%(num))

t=0
while(t<11):
    t+=1
    if(t%2==0):
        continue
    print('Somente impares')
    print(t)
