from main import vcon
import sqlite3
from sqlite3 import Error

def deletar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        
    except Error as ex:
        print (ex)
    finally:
        print("Registro removido")


vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO="
deletar(vcon,vsql)