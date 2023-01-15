from interface import *
import mysql.connector

conexao = mysql.connector.connect(  # funcao que realiza a conexão entre o programa e o BD
    host='localhost',  # passar o host, se o BD estiver no seu computador use local Host
    user='root',  # Usuario do BD
    password='3650',  # Senha do BD
    database='maternidade',  # Nome do esquema que será alterado
) 

cursor = conexao.cursor()

def BD_export_Mae(mae: Mãe):
    comando = f'''INSERT INTO mae (Nome,CPF,Endereco,Telefone,Dt_nasc) VALUES (
                 "{mae.nome}",
                 "{mae.cpf}",
                 "{mae.endereço}",
                 "{mae.telefone}",
                 "{mae.data_nasci}")'''
    cursor.execute(comando)
    conexao.commit()

def BD_export_Bb(bb: Bebê):
    comando = f'''INSERT INTO bebe(
                  Nome,Sexo,Peso,Altura,Nome_mae,CPF_mae,
                  Nome_medico,Data_nasc,Hora_nasc,Codigo_bebe,
                  Cod_parto,Gemeo,Prematuro,Sobreviveu) VALUES(''' 
    pass


def BD_export_medico(medico: Médico):
    comando = f'''INSERT INTO medico (CRM,Especialidade,Nome) VALUES (
                 "{medico.crm}",
                 "{medico.espec}",
                 "{medico.nome}")'''
    cursor.execute(comando)
    conexao.commit()

