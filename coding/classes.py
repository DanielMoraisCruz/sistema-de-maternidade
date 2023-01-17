class Mãe():
    def __init__(self) -> None:
        self.cpf: str = ''
        self.nome: str = ''
        self.endereço: str = ''
        self.telefone: str = ''
        self.data_nasci: str = ''
        self.num_filhos: int = 0
        self.lista_filhos: list = []


class Médico():
    def __init__(self, crm='', espec='', nome='') -> None:
        self.crm: str = crm
        self.espec: str = espec
        self.nome: str = nome


class Parto():
    def __init__(self) -> None:
        self.mãe: Mãe
        self.médico: Médico
        self.cod_parto: int
        self.data_n = "00000000"


class Bebê():
    def __init__(self, mae: Mãe, medico: Médico, parto: Parto) -> None:
        self.nome: str = ''
        self.sexo: str = ''
        self.peso: float = 0.0
        self.altura: float = 0.0
        self.data_nasci: str = ''
        self.hora_nasci: str = ''
        self.sobrevive: bool = True
        self.prematuro: bool = False

        self.mãe: Mãe = mae
        self.médico: Médico = medico
        self.parto: Parto = parto


class Usuario():
    def __init__(self, cpf: str, senha: str) -> None:
        self.cpf: str = cpf
        self.senha: str = senha
