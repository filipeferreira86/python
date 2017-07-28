num1 = int(input('Digite numero de elefantes na musica: '))
s = int(2)

print('1 elefante incomada muita gente')
print('2 elefantes incomodam muito mais...')

while(s<=num1):
    s+=1
    incomodo = 'incomodam '
    print('{} elefantes incomada muita gente'.format(s))
    print('{} elefantes'.format(s+1), incomodo*s,'muito mais...')
    s+=1
else:
    print('Haja elefante, hein??')