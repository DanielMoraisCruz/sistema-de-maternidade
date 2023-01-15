import mysql.connector

conexao = mysql.connector.connect(  # funcao que realiza a conexão entre o programa e o BD
    host='localhost',  # passar o host, se o BD estiver no seu computador use local Host
    user='root',  # Usuario do BD
    password='3650',  # Senha do BD
    database='maternidade',  # Nome do esquema que será alterado
) 

cursor = conexao.cursor()

#inserindo dados
crm = "12345"
especialidade = "parteiro"
nome = "lucas"
comando = f'INSERT INTO medico (CRM,Especialidade,Nome) VALUES ("{crm}", "{especialidade}","{nome}")'
cursor.execute(comando)
conexao.commit() # edita o banco de dado