#operadores lógicos
#duas ou mais condiões verdadeiras (and)
#uma condição ou outra (or)
#Condição negativa (not)
#condição positiva(is)
#esta contido (in)
#negativa de esta contido (not in)
#(is not)

num1 = int(input('digite o primeiro numeo'))
num2 = int(input('Digite outro numeor'))
num3 = int(input('Digite outro numeor'))

if((type(num1) is int or type(num1) is float) and (type(num2) is int or type(num2) is float) and (type(num3) is int or type(num3) is float)):
    if(num1!=num2 and num1==num3):
        print('%d é diferente de %d e igual a %d'%(num1, num2, num3))

    if(num1!=num2 or num1!=num3):
        print('Numero %d é diferente de %d e %d'%(num1, num2, num3))

    if(not(num1==num2)):
        print('%d não é igual a %d'%(num1, num2))
else:
    print('Só numeros por favor')