from main import vcon
import sqlite3
from sqlite3 import Error

def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        #print('Registro inserido')

    except Error as ex:
        print(ex)

r = 'S'

while r == 'S':
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')

    vsql="INSERT INTO tb_contatos(T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO)VALUES('"+nome+"','"+telefone+"','"+email+"')"
    inserir(vcon, vsql)
    r = str(input('Quer cadastrar outra pessoa? [S/N]')).upper()
print('Registro Inserido')
    
