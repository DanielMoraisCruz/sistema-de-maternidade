import mysql.connector
from classes import Bebê, Mãe, Médico, Parto, Usuario

conexao = mysql.connector.connect(  # funcao que realiza a conexão
                                    # entre o programa e o BD
    host='localhost',   # passar o host, se o BD estiver no seu computador use
                        # local Host
    user='root',  # Usuario do BD
    password='OlljFVAZlRVsdNiTncrS',  # Senha do BD
    database='maternidade',  # Nome do esquema que será alterado
)

cursor = conexao.cursor()

#   ----INSERIR INFORMAÇÕES---- #


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
                  Nome_medico,Dt_nasc,Hora_nasc,
                  Cod_parto,Gemeo,Prematuro,Sobreviveu) VALUES(
                  "{bb.nome}",
                  "{bb.sexo}",
                  "{bb.peso}",
                  "{bb.altura}",
                  "{bb.mãe.nome}",
                  "{bb.mãe.cpf}",
                  "{bb.médico.nome}",
                  "{bb.data_nasci}",
                  "{bb.hora_nasci}",
                  "{bb.parto.cod_parto}",
                  "{gemeo}",
                  "{prematuro}",
                  "{sobreviveu}")'''
    cursor.execute(comando)
    conexao.commit()


def BD_export_medico(medico: Médico):
    comando = f'''INSERT INTO medico (CRM,Especialidade,Nome) VALUES (
                 "{medico.crm}",
                 "{medico.espec}",
                 "{medico.nome}")'''
    cursor.execute(comando)
    conexao.commit()


def BD_export_parto(parto: Parto):
    if parto.mãe.num_filhos > 1:
        comando = f'''INSERT INTO parto (CPF_mae, CRM_medico, COD_parto,
                      Dt_parto, Gemeos, Num_Gemeos) VALUES (
                      "{parto.mãe.cpf}",
                      "{parto.médico.crm}",
                      "{parto.cod_parto}",
                      "{parto.data_n}",
                      "{'S'}",
                      "{parto.mãe.num_filhos}")'''
    else:
        comando = f'''INSERT INTO parto (CPF_mae, CRM_medico, COD_parto,
                      Dt_parto, Gemeos) VALUES (
                      "{parto.mãe.cpf}",
                      "{parto.médico.crm}",
                      "{parto.cod_parto}",
                      "{parto.data_n}",
                      "{'N'}")'''
    cursor.execute(comando)
    conexao.commit()


def BD_export_Admin(User: Usuario):
    comando = f'''INSERT INTO admins(CPF,senha) VALUES (
                  "{User.cpf}",
                  "{User.senha}")'''
    cursor.execute(comando)
    conexao.commit()

#   ----VALIDAR INFORMAÇÕES---- #


def BD_Valida_admin(user: Usuario, p_cpf=False):

    if not (p_cpf):
        comando = f'''SELECT cpf FROM maternidade.admins
                      WHERE CPF = "{user.cpf}" AND senha = "{user.senha}"'''
    else:
        comando = f'''SELECT cpf FROM maternidade.admins
                      WHERE CPF = "{user.cpf}"'''
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados
    print(resultado)
    return (False if resultado == [] else True)


def BD_Valida_CPF_Mae(mae: Mãe):
    comando = f'''SELECT CPF FROM maternidade.mae
                  WHERE CPF = "{mae.cpf}"'''
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
    return (False if resultado == [] else True)


def BD_Valida_CRM_Medico(doc: Médico):
    comando = f'''SELECT CRM FROM maternidade.medico
                  WHERE CRM = "{doc.crm}"'''
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
    return (False if resultado == [] else True)


def BD_Valida_parto(parto: Parto):
    comando = f'''SELECT Cod_parto
                 FROM maternidade.parto
                 WHERE "{parto.cod_parto}" = Cod_parto'''
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
    return (False if resultado == [] else True)

    #   ----CONSULTAR INFORMAÇÕES---- #


def BD_getInfo_adim():
    comando = 'SELECT cpf FROM maternidade.admins'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados
    print(resultado)
    return (False if resultado == [] else True)


def BD_getInfo_mae():
    comando = 'SELECT Nome,CPF,Dt_nasc FROM maternidade.mae'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado


def BD_getInfo_medico():
    comando = 'SELECT CRM,Nome FROM maternidade.medico'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados
    print(resultado)
    return (False if resultado == [] else True)


def BD_getInfo_bebe():
    comando = 'SELECT Nome,Sexo,Dt_nasc,Peso,Altura FROM maternidade.bebe'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado


def BD_ConsutaDiaria(data: str):
    comando = f'''SELECT CRM, medico.Nome, parto.CPF_mae, mae.Nome,
                  mae.Dt_nasc,bebe.Nome,Sexo,bebe.Dt_nasc,Peso, Altura
                  FROM maternidade.medico, maternidade.mae,
                  maternidade.bebe, maternidade.parto WHERE
                  Dt_parto = "{data}" AND bebe.Cod_parto = parto.Cod_parto
                  AND CRM_medico = CRM and parto.CPF_mae = CPF'''
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
    return resultado


# ----   PEGA INFORMAÇÕES    ----#

def BD_GetMedico(CRM: str):
    comando = f'''SELECT CRM,Nome
                  FROM maternidade.medico
                  WHERE "{CRM}" = CRM'''
    cursor.execute(comando)
    resultado = list(cursor.fetchall())
    print(resultado)

    return resultado if resultado != [] else ['', '']

# ----   ENCERRAR A CONEXÃO   ----#


def encerrar_conexao():
    cursor.close()
    conexao.close()
# BD_ConsutaDiaria("20000102")
