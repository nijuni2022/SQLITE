from main import vcon

def consultar(conexao, sql):
    
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado
        
#PESQUISA TUDO   
#vsql="SELECT * FROM tb_contatos"
#PESQUISA ESPECIFICA
vsql="SELECT * FROM tb_contatos WHERE T_NOMECONTATO='Nivaldo'"

res=consultar(vcon,vsql)
for r in res:
    print(r)