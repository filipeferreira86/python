#verificadores de idade com if e comparadores compostos

idade = int(input('Qual a sua idade'))

if(idade<=0):
    print('Sua idade não pode ser menor ou igual a 0')
elif(idade>150):
    print('Sua idade não pode sem maior que 150 anos')
elif(idade<18):
    print('Precisa ser maior de 18 anos')
else:
    print('Pronto!!!')