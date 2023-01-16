import mysql.connector
from interface import Bebê, Menu_do_Parto, Mãe, Médico

conexao = mysql.connector.connect(  # funcao que realiza a conexão
                                    # entre o programa e o BD
    host='localhost',   # passar o host, se o BD estiver no seu computador use
                        # local Host
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
    # type: ignore


def BD_export_Bb(bb: Bebê):
    gemeo = 'N'
    if bb.mãe.num_filhos > 1:
        gemeo = 'S'

    prematuro = 'N'
    if bb.prematuro:
        prematuro = 'S'

    sobreviveu = 'N'
    if bb.sobrevive:
        sobreviveu = 'S'

    comando = f'''INSERT INTO bebe(
                  Nome,Sexo,Peso,Altura,Nome_mae,CPF_mae,
                  Nome_medico,Data_nasc,Hora_nasc,
                  Cod_parto,Gemeo,Prematuro,Sobreviveu) VALUES(
                  "{bb.nome}",
                  "{bb.sexo}",
                  "{bb.altura}",
                  "{bb.mãe.nome}",
                  "{bb.mãe.cpf}",
                  "{bb.médico.nome}",
                  "{bb.data_nasci}",
                  "{bb.hora_nasci}",
                  "{bb.parto.cod_parto}",
                  "{gemeo}",
                  "{prematuro}",
                  "{sobreviveu}",)'''
    cursor.execute(comando)
    conexao.commit()


def BD_export_medico(medico: Médico):
    comando = f'''INSERT INTO medico (CRM,Especialidade,Nome) VALUES (
                 "{medico.crm}",
                 "{medico.espec}",
                 "{medico.nome}")'''
    cursor.execute(comando)
    conexao.commit()


def BD_export_parto(parto: Menu_do_Parto):
    if parto.mãe.num_filhos > 1:
        comando = f'''INSERT INTO parto (CPF_mae, CRM_medico, COD_parto,
                      Data_parto, Gemeos, Num_Gemeos) VALUES (
                      "{parto.mãe.cpf}",
                      "{parto.médico.crm}",
                      "{parto.cod_parto}",
                      "{parto.data_n}",
                      "{'S'}",
                      "{parto.mãe.num_filhos}",)'''
    else:
        comando = f'''INSERT INTO parto (CPF_mae, CRM_medico, COD_parto,
                      Data_parto, Gemeos) VALUES (
                      "{parto.mãe.cpf}",
                      "{parto.médico.crm}",
                      "{parto.cod_parto}",
                      "{parto.data_n}",
                      "{'N'}",)'''
    cursor.execute(comando)
    conexao.commit()

def BD_export_Admin(User:Usuario):
    comando = f'''INSERT INTO admins(CPF,senha) VALUES (
                 "{User.cpf}",
                 "{User.senha}",)'''
    cursor.execute(comando)
    conexao.commit()

def BD_getInfo_mae():
    pass


def BD_getInfo_medico():
    pass


def BD_getInfo_bebe():
    pass


def BD_getInfo_partp():
    pass
