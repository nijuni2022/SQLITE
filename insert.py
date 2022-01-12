import sqlite3
from sqlite3 import Error

######### Criar Conexão
def conexaobanco():
    caminho = '/home/nivaldo/Documents/sqlite/SQLITE/agenda.db'
    
    con = None
    try:
        con=sqlite3.connect(caminho)

    except Error as ex:
        print(ex)

    return con

vcon=conexaobanco()

vsql="""INSERT INTO tb_contatos
            (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO)
        VALUES('teste_nome','teste_telefone','teste_email')"""

def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido')

    except Error as ex:
        print(ex)

inserir(vcon, vsql)