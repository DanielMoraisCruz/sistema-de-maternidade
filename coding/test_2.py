import random
from datetime import date

from bancoDeDados import (BD_export_Bb, BD_export_Mae, BD_export_medico,
                          BD_export_parto, BD_Valida_CPF_Mae,
                          BD_Valida_CRM_Medico, BD_Valida_parto)
from interface import Bebê, Mãe, Médico, Parto


def cria_médico():
    medico = Médico()

    crm = "CRM/"
    estados = ['ES', 'SP', 'MG', 'BA', 'RJ']
    x = random.randrange(len(estados))
    y = random.randint(100000, 999999)
    medico.crm = crm + estados[x] + str(y)
    while (BD_Valida_CRM_Medico(medico)):
        x = random.randrange(len(estados))
        y = random.randint(100000, 999999)
        medico.crm = crm + estados[x] + str(y)

    medico.nome = "Genérico"

    return medico


def cria_mãe():
    mae = Mãe()
    mae.cpf = str(random.randint(10000000000, 99999999999))

    while (BD_Valida_CPF_Mae(mae)):
        mae.cpf = str(random.randint(10000000000, 99999999999))

    mae.nome = "Genérica"
    mae.data_nasci = "1111-01-01"
    mae.num_filhos = random.randrange(2)+1
    return mae


def cria_parto(mae: Mãe, medico: Médico):
    parto = Parto()
    parto.mãe = mae
    parto.médico = medico
    parto.cod_parto = str(random.randint(100000, 999999))

    while (BD_Valida_parto(parto)):
        parto.cod_parto = str(random.randint(100000, 999999))

    parto.data_n = str(date.today())

    return parto


def cria_bebe(mae, medico, parto):
    bb = Bebê(mae, medico, parto)

    bb.nome = "Genérico"
    bb.sexo = "M"
    bb.peso = 1.5
    bb.altura = 3.2
    bb.data_nasci = str(date.today())
    bb.hora_nasci = "00:01"
    bb.sobrevive = True
    bb.prematuro = False

    return bb


def gerador_de_parto():
    médico = cria_médico()
    mãe = cria_mãe()
    parto = cria_parto(mãe, médico)

    BD_export_medico(médico)
    BD_export_Mae(mãe)
    BD_export_parto(parto)

    for i in range(mãe.num_filhos):
        bebê = cria_bebe(mãe, médico, parto)
        BD_export_Bb(bebê)


for i in range(5):
    gerador_de_parto()


def GP_2():
    médico = cria_médico()
    mãe = Mãe()
    mãe.cpf = "73369320"
    parto = cria_parto(mãe, médico)

    BD_export_medico(médico)
    BD_export_Mae(mãe)
    BD_export_parto(parto)

    for i in range(mãe.num_filhos):
        bebê = cria_bebe(mãe, médico, parto)
        BD_export_Bb(bebê)
