from main import vcon
import sqlite3
from sqlite3 import Error

def atualizar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        
    except Error as ex:
        print (ex)
    finally:
        print("Dados atualizados")


vsql="UPDATE tb_contatos SET T_NOMECONTATO='Bruno' WHERE N_IDCONTATO=1"
atualizar(vcon,vsql)