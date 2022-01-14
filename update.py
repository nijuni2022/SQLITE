from main import vcon
#import sqlite3
#from sqlite3 import Error

def atualizar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        
    except Error as ex:
        print (ex)
    finally:
        print("Dados atualizados")


vsql="UPDATE tb_contatos SET N_IDCONTATO= 3 WHERE N_IDCONTATO=2"
atualizar(vcon,vsql)