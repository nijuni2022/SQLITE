import sqlite3
from sqlite3 import Error

######### Criar Conexão
def conexaobanco():
    caminho = 'c:\\Users\\junio\\Documents\\SQLITE\\agenda.db'
    con = None
    try:
        con=sqlite3.connect(caminho)

    except Error as ex:
        print(ex)

    return con

vcon=conexaobanco()
