import sqlite3, time

conn = sqlite3.connect('alunos2.db')
c = conn.cursor()


def criar_db():
    c.execute('CREATE TABLE IF NOT EXISTS cadastro(nome text, telefone varchar, email text, data text)')


def inserir(n, t, e):
    d = time.strftime('%d/%m/%Y')
    c.execute('INSERT INTO cadastro VALUES(?, ?, ?, ?)', (n, t, e, d))
    conn.commit()


def pesquisar(p):
    sql = 'SELECT * FROM cadastro WHERE nome = ?'
    for row in c.execute(sql, (p,)):
        print(row)
    print('Deseja alterar e-mail?')


try:
    criar_db()
except:
    print('Erro na geração do BD')
else:
    print('BD criado com sucesso')

fc = input('1 - Cadastrar / 2 - Consultar: ')
if (fc.isnumeric()):
    fc = int(fc)
    if (fc == 1):
        try:
            print('*' * 10, 'Cadastro da agenda', '*' * 10)
            time.sleep(2)
            n = str(input('Digite o nome: '))
            t = str(input('Digite o telefone: '))
            e = str(input('Digite o e-mail: '))
            inserir(n, t, e)
        except:
            print('Erro ao cadastrar')
        else:
            print('Registro criado')
    elif (fc == 2):
        print('*' * 10, 'Busca', '*' * 10)
        n = str(input('Digite o nome: '))
        pesquisar(n)
    else:
        print('...')
else:
    print('Digitar valor válido')
