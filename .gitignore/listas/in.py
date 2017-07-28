#Verificação de itens na lista
alunos = []

def cria_lis():
    print('Informar primeiro nome do aluno ou deixar em branco para finalizar')
    item = input('Nome: ')
    if(item != ''):
        alunos.append(item)
        print('Item adiconado {}'.format(alunos))
        cria_lis()
    else:
        print('Lista concluida: ')
        print(alunos)

def cons_aluno():
    nome1 = input('Digite o nome a ser consultado ou deixe em branco para sair: ')
    if(nome1!=''):
        if(nome1 in alunos):
            print('Aluno consta na lista')
            cons_aluno()
        else:
            print('Aluno não está na lista')
            imprime_alu = input('Deseja ver a lista? ')
            if(imprime_alu in ['s', 'S']):
                print('Lista de alunos:')
                print(alunos)
            inc_alu = input('Deseja incluir {} na lista? '.format(nome1))
            if(inc_alu in ['s', 'S']):
                alunos.append(nome1)
                cons_aluno()

print('*'*10, 'Criação da lista', '*'*10)
cria_lis()



print('Deseja consultar algum aluno:')
cons_al = input('Digite S para consultar: ')
if(cons_al in ['s', 'S']):
    print('*' * 10, 'Consulta:', '*' * 10)
    cons_aluno()
else:
    print('Muito obrigado')
    pass

print('Muito obrigado')