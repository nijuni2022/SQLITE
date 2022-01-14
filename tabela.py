from main import vcon
#import sqlite3
#from sqlite3 import Error



vsql="""CREATE TABLE tb_contatos(
            # N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            # T_NOMECONTATO VARCHAR(30),
            # T_TELEFONECONTATO VARCHAR(14),
            # T_EMAILCONTATO VARCHAR(30),
            T_CPF VARCHAR(14)
        );"""


def criartabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print('Tabela criada')

    except Error as ex:
        print(ex)

criartabela(vcon,vsql)
vcon.close()