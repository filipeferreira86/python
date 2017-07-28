# Import da biblioteca SQLITE
import sqlite3

# Criando constante com o caminho para o bd
path = r'c:\sqlite\estudos'

# var conexção com bd o banco será TESTE.DB dentro da pasta indicada no path
conn = sqlite3.connect(path + r'\teste.bd')

# Cursor vai me permitir executar comandos no bd SQL que logamos no connect
# Para tal crio uma variavel que recebe uma instancia da var com a conexção + o comando cursor
c = conn.cursor()


# Aqui estou criando uma tabela dentro do meu BD teste.bd
def create():
    c.execute('CREATE TABLE IF NOT EXISTS dados  (id integer, unix real, keyword text);')


create()


# Informando dados para a tabela:
def entrada():
    c.execute('INSERT INTO dados VALUES(1, 2.3, "Filipe")')
    c.execute('INSERT INTO dados VALUES(2, 2.3, "Aline")')
    c.execute('INSERT INTO dados VALUES(3, 2.3, "Marcio")')
    # O commit grava os dados no bd
    conn.commit()


entrada()

alunos = c.execute('select * from dados')
print(list(alunos))

# Sempre lembrar de fechar a conexção
conn.close()
