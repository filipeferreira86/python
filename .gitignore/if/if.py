#Autor: Filipe Ferreira de Jesus
#Motivo: Aula if
#Data: 24/06/2017

num2 = int(input('Digite o segundo numero? '))
num = int(input('Digite um numero: '))
if(num==num2):
    print('Numeros iguais!!!')

    #elif significa que estamos utilisando um else mas teremos mais alguma condição
elif(num>num2):
    print('{} é maior que {}'.format(num, num2))

else:
    print('{} é menor que {}'.format(num, num2))
