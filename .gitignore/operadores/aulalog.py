login = input('Login: ')
senha = input('Senha: ')
print('Seu login é: {}'.format(login))

# Operadores aritimeticos
# Soma
rsum = 5+2
#subtração
rsub = 5-2
#divisão
rdiv = 5/2
#divisão inteira
rdivi = 5//2
#Resto da divisão
rrest = 5%2
#multiplicação
rmult = 5*2
#potencia
rpot = 5**2
#raiz
rraiz = 5*(.5)

#prints
print('{} relações entre 5 e 2 {}'.format(10*'*', 10*'*'));
print ('Soma: {}\nSutração: {}\nDivisão: {}\nDivisão Inteira: {}\nResto da divisão: {}\nMultiplicação: {}\nPotencia: {}\nRaiz: {}'.format(rsum, rsub, rdiv, rdivi, rrest,
                                                                                                                                          rmult, rpot, rraiz))

#Operadores comparativo (Booleanos)
#Neste caso ele irá verificar se os valores são iguais, caso positivo ele armazenará o valor verdadeiro(true) caso negativo falso (false)
compf = rsum == rsub
#Operador de diferença
compv = rsum != rsub

print('Valor positivo: {}\nValor negativo: {}'.format(compv, compf))

#Menor que
compmen = rsum < rsub
#maior que
compmai = rsum > rsub

print('Valor positivo: {}\nValor negativo: {}'.format(compmai, compmen))

teste = int(input('Numero:'))

#maior ou igual
comp1 = teste <= rsum
#menor ou igual
comp2 = teste >= rsum

print('Seu valor é menor ou igual a soma de 5+2: {}\nValor maior ou igual a soma de 5+2: {}'.format(comp1, comp2))