#Verificação de itens na lista

import sqlite3

conn = sqlite3.connect('alunos.bd')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS alunos2 (mat integer, nome text, sobrenome text, nota_a real, notab real, regular text)')


def cons_aluno(nome1):
    if(nome1!=''):
        aluno1 = cursor.execute('SELECT * FROM alunos2 WHERE nome = ?',[nome1])
        aluno1 = list(aluno1)
        if(aluno1):
            dados = aluno1[0]
            print('Aluno: {} Matrucila {} está {}'.format(dados[1], dados[0], dados[-1]))
        else:
            print('Aluno não está matriculado')


def inc_alunos(nom, sob):
    mat_lis = list(cursor.execute('SELECT * FROM alunos2'))
    if(mat_lis):
        ult_mat = mat_lis[-1]
        nova_mat = (int(ult_mat[0])+1)
        cursor.execute('INSERT INTO alunos2(mat, nome, sobrenome, nota_a, \
        notab ) VALUES(?, ?, ?, 0.0, 0.0)',(nova_mat, nom, sob))
        conn.commit()
        return nova_mat

    else:
        nova_mat = 1
        cursor.execute('INSERT INTO alunos2(mat, nome, sobrenome, nota_a, \
        notab ) VALUES(?, ?, ?, 0.0, 0.0)',(nova_mat, nom, sob))
        conn.commit()
        return nova_mat


def cria_lis():
    print('Deseja matricular novo aluno?')
    mat = input('S para sim: ')
    if (mat == 'S' or mat == 's'):
        nome = input('Nome do aluno: ')
        sob = input('Sobrenome do aluno: ')
        print('Matricula realisada {}'.format(inc_alunos(nome, sob)))
        cria_lis()
    else:
        print('Lista concluida: ')



print('*'*10, 'Matricular', '*'*10)
cria_lis()



print('Deseja consultar algum aluno:')
cons_al = input('Digite S para consultar: ')
if(cons_al in ['s', 'S']):
    print('*' * 10, 'Consulta:', '*' * 10)
    nome_aluno = input('Nome do aluno: ')
    cons_aluno(nome_aluno)
else:
    print('Muito obrigado')
    pass

print('Muito obrigado')