#import
import time # esta bibloteca permite buscar data atual em unix
import datetime # esta bibloteca permite transformar unix em data
import sqlite3

caminho = r'C:\Users\filipe.de.jesus\PycharmProjects\sqlite\estudos'

con = sqlite3.connect(caminho+r'\alunos.bd')

cursor = con.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS alunos (Matricula integer, Nome text\
,Nota_1 real,Nota_2 real,Data_da_matricula text)')

mat = 1
nome = 'Aline'
notaa = 0.0
notab = 0.0

def entrada():
    # Busca data em unix
    unix = int(time.time())
    # Trasnformaesta informação em uma lista (Ano, mes, dia, hora, min, seg, mseg)
    dataint = datetime.datetime.fromtimestamp(unix)
    # Trasnformar data em formarto desejado sendo d dia, m mes, Y ano, H hora, M minuto, S segundo
    date = str(dataint.strftime('%d/%m/%Y %H:%M:%S'))
    # Pode ser escrito como abaixo mas fica muito feioooooo
    #date1 = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%d/%m/%Y'))
    cursor.execute('INSERT INTO alunos (Matricula , Nome ,Nota_1 ,Nota_2\
    , Data_da_matricula) VALUES(?,?,?,?,?)',(mat, nome, notaa, notab, time.time()))
    con.commit()

entrada()
teste = list(cursor.execute('select * from alunos'))
print (teste)
con.close()