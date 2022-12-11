import tkinter as tk

# from datetime import date, tim


class Iniciar_sistema():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.tela()
        self.frames_da_tela()
        self.Menu_inicial = Menu_inicial(self)
        self.Parto = Menu_do_Parto(self)
        self.Médicos = Menu_do_Médico(self)

        self.Menu_inicial.cria_Menu()
        self.root.mainloop()

    def tela(self):
        self.root.title("Menu Inicial")
        self.root.geometry("700x500")
        self.root.config(background='lightblue')

    def frames_da_tela(self):
        self.tela_ = tk.Frame(self.root)
        self.tela_.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        # self.tela_.config(background='Blue')

        self.tab = tk.Label(self.tela_)
        self.tab.grid(column=0, row=1, padx=2, pady=2)
        self.tab_2 = tk.Label(self.tela_)
        self.tab_2.grid(column=0, row=0, padx=2, pady=2)


class Menu_inicial():
    def __init__(self, base: Iniciar_sistema) -> None:
        self.base = base

    def cria_Menu(self):
        self.intro = tk.Label(
            self.base.tela_,
            text="Selecione a Opção de Cadastro"
        )
        self.intro.grid(
            column=1, row=1,
            padx=0.5, pady=0.5,
            sticky='W'
        )

        self.bt_parto = tk.Button(
            self.base.tela_,
            text="Cadastrar Parto",
            command=self.base.Parto.cria_Parto
        )
        self.bt_parto.grid(column=2, row=1, padx=0.5, pady=0.5)

        self.bt_médico = tk.Button(
            self.base.tela_,
            text="Cadastrar Médico",
            command=self.base.Médicos.cria_Médico
        )
        self.bt_médico.grid(column=3, row=1, padx=0.5, pady=0.5)

    def fechar_Menu(self):
        self.intro.destroy()
        self.bt_parto.destroy()
        self.bt_médico.destroy()


class Menu_do_Parto():
    def __init__(self, base: Iniciar_sistema) -> None:
        self.base = base

        self.status_mãe: bool = False
        self.erro_mostrado: bool = False
        self.enviado: bool = False

        self.mãe: Mãe = Mãe()
        self.médico: Médico = Médico()
        self.bebê: Bebê = Bebê(self)

    def cria_Parto(self):
        self.base.Menu_inicial.fechar_Menu()

        # Informações do Médico
        self.info_médico = tk.Label(
            self.base.tela_,
            text="CRM do Médico Responsável: ",
        )
        self.info_médico.grid(
            column=1, row=1,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.caixa_crm = tk.Entry(self.base.tela_)
        self.caixa_crm.grid(
            column=2, row=1, columnspan=2,
            padx=0.5, pady=0.5
        )

        self.caixa_crm.focus()

        # Pedir informações da mãe
        self.info_mãe = tk.Label(
            self.base.tela_,
            text="Mãe cadastrada? ",
        )
        self.info_mãe.grid(
            column=1, row=2,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        # A mãe já está no sistema?
        self.valida = tk.BooleanVar()

        self.var_0 = tk.Radiobutton(
            self.base.tela_,
            text='Sim',
            variable=self.valida,
            value=True,
            command=self.deleta_cadastrar_mãe
        )
        self.var_1 = tk.Radiobutton(
            self.base.tela_,
            text='Não',
            variable=self.valida,
            value=False,
            command=self.cadastrar_mãe
        )

        self.var_0.grid(column=2, row=2, padx=0.5, pady=0.5)
        self.var_1.grid(column=3, row=2, padx=0.5, pady=0.5)

        self.var_0.select()

        # CPF
        self.info_cpf = tk.Label(
            self.base.tela_,
            text="CPF: ",
        )
        self.info_cpf.grid(
            column=1, row=3,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.cpf = tk.Entry(self.base.tela_)
        self.cpf.grid(
            column=2, row=3, columnspan=2,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        # Definir Numero de Recém Nascido
        self.info_número_rn = tk.Label(
            self.base.tela_,
            text='Número de Recém Nascidos:'
        )
        self.info_número_rn.grid(
            column=1, row=8,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.número_rn = tk.Entry(self.base.tela_)
        self.número_rn.grid(
            column=2, row=8,
            padx=0.5, pady=0.5,
            sticky='W'
        )

        # Botão de Enviar
        self.bt_enviar = tk.Button(
            self.base.tela_,
            text='Enviar',
            command=self.enviar
        )
        self.bt_enviar.grid(column=4, row=10, sticky='E')

        # Botão Voltar
        self.bt_voltar_parto = tk.Button(
            self.base.tela_,
            text="Voltar",
            command=self.voltar
        )
        self.bt_voltar_parto.grid(column=1, row=10, sticky='W')

    def cadastrar_mãe(self):
        if self.status_mãe:
            print('Não Criou as informações')
            return
        print('Criou as informações')
        # Nome
        self.informe_nome_mãe = tk.Label(
            self.base.tela_,
            text="Nome: ",
        )
        self.informe_nome_mãe.grid(
            column=1, row=4,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.nome_mãe = tk.Entry(self.base.tela_)
        self.nome_mãe.grid(
            column=2, row=4, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        # Endereço
        self.informe_endereço = tk.Label(
            self.base.tela_,
            text="Endereço: ",
        )
        self.informe_endereço.grid(
            column=1, row=5,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.endereço = tk.Entry(self.base.tela_)
        self.endereço.grid(
            column=2, row=5, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        # Telefone
        self.informe_telefone = tk.Label(
            self.base.tela_,
            text="Telefone: ",
        )
        self.informe_telefone.grid(
            column=1, row=6,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.telefone = tk.Entry(self.base.tela_)
        self.telefone.grid(
            column=2, row=6, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        # Data Nascimento
        self.informe_data_n = tk.Label(
            self.base.tela_,
            text="Data de Nascimento: ",
        )
        self.informe_data_n.grid(
            column=1, row=7,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.data_n = tk.Entry(self.base.tela_)
        self.data_n.grid(
            column=2, row=7, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        self.status_mãe = True

    def deleta_cadastrar_mãe(self):
        if not (self.status_mãe):
            print('Não deletou')
            return

        print('Deletou tudo')
        self.informe_nome_mãe.destroy()
        self.nome_mãe.destroy()
        self.informe_endereço.destroy()
        self.endereço.destroy()
        self.informe_telefone.destroy()
        self.telefone.destroy()
        self.informe_data_n.destroy()
        self.data_n.destroy()

        self.status_mãe = False

    def voltar(self):
        self.enviado = False
        self.fechar_Parto()

    def fechar_Parto(self):
        valor = int(self.número_rn.get()) if self.número_rn.get() != '' else 0
        print(self.erro_mostrado)
        print(self.enviado, "AAAA")
        if self.enviado and valor <= 0:
            if not (self.erro_mostrado):
                print("Error - Numero de Recém Nascidos INVALIDO")
                self.error_message_1 = tk.Label(
                    self.base.tela_,
                    text='Error - Numero de Recém Nascidos INVALIDO'
                )
                self.error_message_1.grid(column=5, row=10, sticky='E')
                self.erro_mostrado = True
            self.enviado = False
            return

        self.info_médico.destroy()
        self.caixa_crm.destroy()
        self.info_mãe.destroy()
        self.bt_enviar.destroy()
        self.var_0.destroy()
        self.var_1.destroy()
        self.info_cpf.destroy()
        self.cpf.destroy()

        if self.erro_mostrado:
            self.erro_mostrado = False
            self.error_message_1.destroy()

        if self.status_mãe:
            self.deleta_cadastrar_mãe()

        self.info_número_rn.destroy()
        self.número_rn.destroy()

        self.bt_voltar_parto.destroy()

        if not (self.enviado):
            self.base.Menu_inicial.cria_Menu()
        else:
            self.bebê.cadastrar_bebê(self)

    def enviar(self):
        self.mãe.cpf = self.cpf.get()

        if not (self.valida):
            self.mãe.nome = self.nome_mãe.get()
            self.mãe.endereço = self.endereço.get()
            self.mãe.telefone = self.telefone.get()
            self.mãe.data_nasci = self.data_n.get()
        else:
            self.mãe.nome = 'default'
            self.mãe.endereço = 'default'
            self.mãe.telefone = 'default'
            self.mãe.data_nasci = '00-00-00'

        enviar_dado_mãe(self.mãe)
        self.enviado = True
        self.fechar_Parto()


class Menu_do_Médico():
    def __init__(self, base: Iniciar_sistema) -> None:
        self.base = base

    def cria_Médico(self):
        self.base.Menu_inicial.fechar_Menu()
        self.intro = tk.Label(
            self.base.tela_,
            text="Cadastre o médico"
        )
        self.intro.place(relx=0.01, rely=0.1)

        # Botão Voltar
        self.bt_voltar_médico = tk.Button(
            self.base.tela_,
            text="Voltar",
            command=self.limpar_médico
        )
        self.bt_voltar_médico.place(relx=0.83, rely=0.85,
                                    relwidth=0.15, relheight=0.1)

    def fechar_Médico(self):

        self.base.Menu_inicial.cria_Menu()


class Bebê():
    def __init__(self, parto: Menu_do_Parto) -> None:
        self.parto: Menu_do_Parto = parto
        self.base: Iniciar_sistema = self.parto.base
        self.nome: str = ''
        self.sexo: str = ''
        self.peso: float = 0.0
        self.altura: float = 0.0
        self.data_nasci: str = ''
        self.hora_nasci: str = ''
        self.sobrevive: bool = True
        self.prematuro: bool = False

        self.médico: Médico = self.parto.médico
        self.mãe: Mãe = self.parto.mãe

    def cadastrar_bebê(self, numero: int = 0):
        self.numero = numero

        # self.nome: str
        self.informe_nome = tk.Label(
            self.base.tela_,
            text="Nome: ",
        )
        self.informe_nome.grid(
            column=1, row=1,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.nome_bebê = tk.Entry(self.base.tela_)
        self.nome_bebê.grid(
            column=2, row=1, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        # self.sexo: enumerate
        self.informe_sexo = tk.Label(
            self.base.tela_,
            text="Sexo: ",
        )
        self.informe_sexo.grid(
            column=1, row=2,
            padx=0.5, pady=0.5,
            sticky='E'
        )
        self.sexo_bebe = tk.StringVar()

        self.var_0 = tk.Radiobutton(
            self.base.tela_,
            text='M',
            variable=self.sexo_bebe,
            value='M'
        )
        self.var_1 = tk.Radiobutton(
            self.base.tela_,
            text='F',
            variable=self.sexo_bebe,
            value='F'
        )
        self.var_2 = tk.Radiobutton(
            self.base.tela_,
            text='O',
            variable=self.sexo_bebe,
            value='O'
        )

        self.var_0.grid(column=2, row=2, padx=0.5, pady=0.5)
        self.var_1.grid(column=3, row=2, padx=0.5, pady=0.5)
        self.var_2.grid(column=4, row=2, padx=0.5, pady=0.5)

        # self.peso: float
        self.informe_peso = tk.Label(
            self.base.tela_,
            text="Peso: ",
        )
        self.informe_peso.grid(
            column=1, row=4,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.peso_bebê = tk.Entry(self.base.tela_)
        self.peso_bebê.grid(
            column=2, row=4, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        # self.altura: float
        self.informe_altura = tk.Label(
            self.base.tela_,
            text="Altura: ",
        )
        self.informe_altura.grid(
            column=1, row=5,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.altura_bebê = tk.Entry(self.base.tela_)
        self.altura_bebê.grid(
            column=2, row=5, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        # self.data_nasci: date
        self.informe_data = tk.Label(
            self.base.tela_,
            text="Data do Nascimento: ",
        )
        self.informe_data.grid(
            column=1, row=6,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.data_bebê = tk.Entry(self.base.tela_)
        self.data_bebê.grid(
            column=2, row=6, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        # self.hora_nasci: time
        self.informe_hora = tk.Label(
            self.base.tela_,
            text="Hora do Nascimento: ",
        )
        self.informe_hora.grid(
            column=1, row=7,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.hora_bebê = tk.Entry(self.base.tela_)
        self.hora_bebê.grid(
            column=2, row=7, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        # Prematuro
        self.informe_prematuro = tk.Label(
            self.base.tela_,
            text="Prematuro? ",
        )
        self.informe_prematuro.grid(
            column=1, row=8,
            padx=0.5, pady=0.5,
            sticky='E'
        )
        self.pre_bebê = tk.BooleanVar()

        self.var_pre_0 = tk.Radiobutton(
            self.base.tela_,
            text='Sim',
            variable=self.pre_bebê,
            value=True
        )
        self.var_pre_1 = tk.Radiobutton(
            self.base.tela_,
            text='Não',
            variable=self.pre_bebê,
            value=False
        )

        self.var_pre_0.grid(column=2, row=8, padx=0.5, pady=0.5)
        self.var_pre_1.grid(column=3, row=8, padx=0.5, pady=0.5)

        # sobreviveu?
        self.informe_sobreviveu = tk.Label(
            self.base.tela_,
            text="Sobreviveu? ",
        )
        self.informe_sobreviveu.grid(
            column=1, row=9,
            padx=0.5, pady=0.5,
            sticky='E'
        )
        self.sob_bebê = tk.BooleanVar()

        self.var_sobreviveu_0 = tk.Radiobutton(
            self.base.tela_,
            text='Sim',
            variable=self.sob_bebê,
            value=True
        )
        self.var_sobreviveu_1 = tk.Radiobutton(
            self.base.tela_,
            text='Não',
            variable=self.sob_bebê,
            value=False
        )

        self.var_sobreviveu_0.grid(column=2, row=9, padx=0.5, pady=0.5)
        self.var_sobreviveu_1.grid(column=3, row=9, padx=0.5, pady=0.5)
        self.var_sobreviveu_0.select()

        # Botão de Enviar
        self.bt_enviar = tk.Button(
            self.base.tela_,
            text='Enviar',
            command=self.enviar
        )
        self.bt_enviar.grid(column=4, row=10, sticky='E')

        # Botão Voltar
        self.bt_voltar_parto = tk.Button(
            self.base.tela_,
            text="Voltar",
            command=self.fechar_bebê
        )
        self.bt_voltar_parto.grid(column=1, row=10, sticky='W')

    def fechar_bebê(self):
        self.informe_nome.destroy()
        self.nome_bebê.destroy()
        self.informe_sexo.destroy()
        self.var_0.destroy()
        self.var_1.destroy()
        self.informe_peso.destroy()
        self.peso_bebê.destroy()
        self.informe_altura.destroy()
        self.altura_bebê.destroy()
        self.informe_data.destroy()
        self.data_bebê.destroy()
        self.informe_hora.destroy()
        self.hora_bebê.destroy()
        self.informe_prematuro.destroy()
        self.var_pre_0.destroy()
        self.var_pre_1.destroy()
        self.informe_sobreviveu.destroy()
        self.var_sobreviveu_0.destroy()
        self.var_sobreviveu_1.destroy()
        self.bt_voltar_parto.destroy()
        self.bt_enviar.destroy()
        self.parto.cria_Parto()

    def enviar(self):

        self.nome = self.nome_bebê.get()
        self.sexo = self.sexo_bebe.get()
        self.peso = self.peso_bebê.get()
        self.altura = self.altura_bebê.get()
        self.data_nasci = self.data_bebê.get()
        self.hora_nasci = self.hora_bebê.get()
        self.prematuro = self.pre_bebê.get()
        self.sobrevive = self.sob_bebê.get()

        # envia os dados para o
        enviar_dado_bebê(self)

        self.nome = ''
        self.sexo = ''
        self.peso = 0.0
        self.altura = 0.0
        self.data_nasci = ''
        self.hora_nasci = ''
        self.sobrevive = True
        self.prematuro = False

        self.fechar_bebê()
        if (self.numero-1) >= 0:
            self.cadastrar_bebê(self, self.numero-1)
        else:
            print("Todos os Bebês foram Cadastrados")
            self.fechar_bebê()


class Mãe():
    def __init__(self) -> None:
        self.cpf: str = ''
        self.nome: str = ''
        self.endereço: str = ''
        self.telefone: str = ''
        self.data_nasci: str = ''


class Médico():
    def __init__(self) -> None:
        self.crm: str = ''
        self.espec: str = ''
        self.nome: str = ''


def enviar_dado_bebê(bebe: Bebê):
    print(f"""
    Estas informações devem ser enviadas para o Banco
    Nome do bebê: {bebe.nome}
    Sexo do bebê: {bebe.sexo}
    Peso do bebê: {bebe.peso}
    Altura do bebê: {bebe.altura}
    Data de Nascimento do bebê: {bebe.data_nasci}
    Horário de Nascimento do bebê: {bebe.hora_nasci}
    Prematuro? {bebe.prematuro}
    Sobreviveu?: {bebe.sobrevive}
    """)


def enviar_dado_mãe(mãe: Mãe):
    print(mãe.nome)


def enviar_dado_médico(médico: Médico):
    print(médico.nome)


Iniciar_sistema()
