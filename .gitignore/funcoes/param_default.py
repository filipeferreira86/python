# Parametros que são facultativos
# Os parametros que não tem default devem ser os primeiros a serem declarados
def login(user='root', password=123):
    print('Usuário: {}'.format(user))
    print('Senha: {}'.format(password))

login('claudio', 12345)