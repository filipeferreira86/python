#Propriedades da string
#tamanho
s = 'Lista de caracteres'
print(len(s))

#alterar uma string
s1, s2, s3 = s[0:6], s[6:9], s[9:]
print(s1, s2, s3)
s4 = s1+s3
print(s4)

#agora do jeito facil
#a função split vai retornar os caracteres divididos em lista separados com o delimitador informado conforme abaixo:
ssep = s.split(' ')
print(ssep)
s13 = ssep[0]+' '+ssep[2]
print(s13)
print(type(s13))
#mais facil aindaaaaaaaa
ss = s.split('de')