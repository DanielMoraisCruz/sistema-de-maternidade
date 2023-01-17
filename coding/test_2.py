from bancoDeDados import (BD_export_Bb, BD_export_Mae,
                          BD_export_medico, BD_export_parto,
                          BD_Valida_CPF_Mae, BD_Valida_CRM_Medico)
from interface import Bebê, Mãe, Médico, Parto

medico = Médico(
    crm="CRM/ES123456",
    espec='',
    nome='Pedro'
)

mae = Mãe()
mae.cpf = "96001372268"
mae.nome = "ame"
mae.data_nasci = "1111-01-01"
mae.num_filhos = 1


parto = Parto()
parto.mãe = mae
parto.médico = medico
parto.cod_parto = "123472111"
parto.data_n = '2023-11-12'

bebe = Bebê(
    mae,
    medico,
    parto
)

bebe.nome = 'aaa'
bebe.sexo = "M"
bebe.peso = 1
bebe.altura = 1
bebe.data_nasci = '2023-11-22'
bebe.hora_nasci = '00:00'
bebe.sobrevive = True
bebe.prematuro = False

if not BD_Valida_CRM_Medico(medico):
    BD_export_medico(medico)

if not (BD_Valida_CPF_Mae(mae)):
    BD_export_Mae(mae)
    BD_export_parto(parto)

BD_export_Bb(bebe)