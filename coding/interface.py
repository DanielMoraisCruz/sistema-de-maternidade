import tkinter as tk

from bancoDeDados import BD_export_Admin, BD_getInfo_adim, BD_Valida_admin
from classes import Bebê, Mãe, Médico, Parto, Usuario


class Iniciar_sistema():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.tela()
        self.frames_da_tela()
        self.Menu_inicial = Menu_inicial(self)
        self.Parto = Menu_do_Parto(self)
        self.Médicos = Menu_do_Médico(self)

        self.erro = False
        self.bt1_ = False

        self.escolha_inicial()
        self.root.mainloop()

    def tela(self):
        self.root.title("MATERNIDADE MARIA")
        self.root.config(background='lightblue')
        self.root.geometry("700x500")
        self.root.resizable(False, False)

    def frames_da_tela(self):
        self.tela_ = tk.Frame(self.root)
        self.tela_.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        # self.tela_.config(background='Blue')

        self.tab = tk.Label(self.tela_)
        self.tab.grid(column=0, row=1, padx=2, pady=2)
        self.tab_2 = tk.Label(self.tela_)
        self.tab_2.grid(column=0, row=0, padx=2, pady=2)

    def escolha_inicial(self):
        if BD_getInfo_adim():
            self.bt1 = tk.Button(self.tela_, text="Fazer Login",
                                 command=self.enviar_login)
            self.bt1.grid(column=1, row=1, padx=2, pady=2)
            self.bt1_ = True

        self.bt2 = tk.Button(self.tela_, text="Cadastrar",
                             command=self.enviar_cadastro)
        self.bt2.grid(column=2, row=1, padx=2, pady=2)

    def enviar_login(self):
        self.bt1.destroy()
        self.bt2.destroy()
        self.tela_login()

    def enviar_cadastro(self):
        if self.bt1_:
            self.bt1.destroy()
        self.bt2.destroy()
        self.tela_login(True)

    def tela_login(self, x=False):
        self.x = x
        self.cpf = tk.Label(
            self.tela_,
            text="CPF:"
        )
        # self.login.place(relheight=0.1, relwidth=0.1)
        self.cpf.grid(column=1, row=1, padx=2, pady=2)

        self.cpf_En = tk.Entry(self.tela_)
        # self.login_En.place(relheight=0.01, relwidth=0.1)
        self.cpf_En.grid(column=2, row=1, padx=2, pady=2)

        self.senha = tk.Label(
            self.tela_,
            text="Senha:"
        )
        self.senha.grid(column=1, row=2, padx=2, pady=2)

        self.senha_En = tk.Entry(self.tela_)
        self.senha_En.grid(column=2, row=2, padx=2, pady=2)

        if not (self.x):
            self.bt1 = tk.Button(self.tela_, text="Confirmar",
                                 command=self.validar_senha)
            self.bt1.grid(column=1, row=3, padx=2, pady=2, columnspan=2)
        else:
            self.bt2 = tk.Button(self.tela_, text="Cadastrar",
                                 command=self.cadastrar)
            self.bt2.grid(column=2, row=3, padx=2, pady=2, columnspan=2)

    def validar_senha(self):
        cpf = self.cpf_En.get()
        self.alter_cpf = cpf
        if (cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'):
            self.alter_cpf = (cpf[0:3]+cpf[4:7] +
                              cpf[8:11]+cpf[12:14])  # 012.456.890-90

        self.user = Usuario(self.alter_cpf, self.senha_En.get())

        if BD_Valida_admin(self.user) and len(self.alter_cpf) < 11:
            self.deleta_login()
            self.Menu_inicial.cria_Menu()
        else:
            self.erro_de_login()
            return

    def cadastrar(self):
        cpf = self.cpf_En.get()

        self.alter_cpf = (cpf[0:3]+cpf[4:7] +
                          cpf[8:11]+cpf[12:14])

        if len(self.alter_cpf) < 11:
            self.erro_de_login()
            return

        print(self.alter_cpf)
        self.user = Usuario(self.alter_cpf, self.senha_En.get())
        
        if BD_Valida_admin(self.user, True):
            print('CPF Já está Cadastrado')
            self.erro_de_login('ou Já está Cadastrado')
        
        BD_export_Admin(self.user)

    def erro_de_login(self, texto):
        if not (self.erro):
            self.er_senha = tk.Label(
                self.tela_,
                text=f"""Senha ou CPF Incorreto {texto}
                        Tente inserir com a pontuação 000.000.000-00
                     """,
                border=1,
                background='grey',
            )
            self.er_senha.grid(
                column=0, row=10,
                padx=2, pady=2, columnspan=2,
                sticky='WE'
            )
            self.erro = True

    def deleta_login(self):
        self.cpf.destroy()
        self.senha.destroy()
        self.cpf_En.destroy()
        self.senha_En.destroy()
        if self.erro:
            self.er_senha.destroy()

        self.bt1.destroy() if not (self.x) else self.bt2.destroy()


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

    def receber_info_mãe(self):
        # ----  PEGAR INFOS DE MÃE  ---- #
        pass

    def receber_info_médico(self):
        # ----  PEGAR INFOS DE MÉDICO  ---- #
        pass

    def receber_info_bebê(self):
        # ----  PEGAR INFOS DE BEBÊ  ---- #
        pass


class Menu_do_Parto():
    def __init__(self, base: Iniciar_sistema) -> None:
        self.base = base
        self.parto: Parto = Parto()

        self.status_mãe: bool = False

        self.erro_mostrado_1: bool = False
        self.erro_mostrado_2: bool = False

        self.val_erro: bool = True

        self.enviado: bool = False

    def cria_Parto(self):

        self.status_mãe = False
        self.erro_mostrado_1 = False
        self.erro_mostrado_2 = False
        self.enviado = False

        self.parto.mãe = Mãe()
        self.parto.médico = Médico()
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
        self.val_erro = False
        self.fechar_Parto()

    def fechar_Parto(self):
        valor = int(self.número_rn.get()) if self.número_rn.get() != '' else 0

        if self.enviado and valor <= 0:
            if not (self.erro_mostrado_1):
                print("Error - Numero de Recém Nascidos INVALIDO")
                self.error_message_1 = tk.Label(
                    self.base.tela_,
                    text='Error - Numero de Recém Nascidos INVALIDO'
                )
                self.error_message_1.grid(column=5, row=10, sticky='E')
                self.erro_mostrado_1 = True
            self.enviado = False
            return

        if self.enviado and (self.cpf.get() == '' or
                             self.caixa_crm.get() == ''):
            if not (self.erro_mostrado_2):
                print("Error - Insira o CPF da Mãe e o CRM do Médico")
                self.error_message_2 = tk.Label(
                    self.base.tela_,
                    text="Error - Insira o CPF da Mãe e o CRM do Médico"
                )
                self.error_message_2.grid(column=5, row=11, sticky='E')
                self.erro_mostrado_2 = True
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

        if self.erro_mostrado_1:
            self.erro_mostrado_1 = False
            self.error_message_1.destroy()

        if self.erro_mostrado_2:
            self.erro_mostrado_2 = False
            self.error_message_2.destroy()

        if self.status_mãe:
            self.deleta_cadastrar_mãe()

        self.info_número_rn.destroy()
        self.número_rn.destroy()

        self.bt_voltar_parto.destroy()

        if not (self.enviado):
            self.base.Menu_inicial.cria_Menu()
        else:
            # ---- ENVIA PARTO ----#

            # ---- PEGA COD_PARTO ----#
            self.cod_parto = 0
            self.inserir_bebês()

    def inserir_bebês(self):
        bebe_temp = Menu_do_Bebê(self)
        bebe_temp.cadastrar_bebê()

    def enviar(self):
        self.parto.mãe.cpf = self.cpf.get()

        if not (self.valida):
            self.parto.mãe.nome = self.nome_mãe.get()
            self.parto.mãe.endereço = self.endereço.get()
            self.parto.mãe.telefone = self.telefone.get()
            self.parto.mãe.data_nasci = self.data_n.get()
        else:
            self.parto.mãe.nome = 'default'
            self.parto.mãe.endereço = 'default'
            self.parto.mãe.telefone = 'default'
            self.parto.mãe.data_nasci = '0000-00-00'

        self.parto.mãe.num_filhos = int(self.número_rn.get())

        # ----  ENVIAR MÃE  ---- #

        self.enviado = True
        self.fechar_Parto()


class Menu_do_Médico():
    def __init__(self, base: Iniciar_sistema) -> None:
        self.base = base
        self.lista_médicos: list = []
        self.val_erro: bool = True

    def cria_Médico(self):
        self.base.Menu_inicial.fechar_Menu()

        # Informações do Médico
        self.info_médico = tk.Label(
            self.base.tela_,
            text="Para cadastrar os Médicos preencha as informações a baixo: ",
        )
        self.info_médico.grid(
            column=1, row=1, columnspan=10,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        # CRM
        self.info_CRM = tk.Label(
            self.base.tela_,
            text="CRM: ",
        )
        self.info_CRM.grid(
            column=1, row=2,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.CRM = tk.Entry(self.base.tela_)
        self.CRM.grid(
            column=2, row=2, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        # Especialidade
        self.info_espec = tk.Label(
            self.base.tela_,
            text="Especialidade: ",
        )
        self.info_espec.grid(
            column=1, row=3,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.espec = tk.Entry(self.base.tela_)
        self.espec.grid(
            column=2, row=3, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        # Nome
        self.info_nome = tk.Label(
            self.base.tela_,
            text="Nome: ",
        )
        self.info_nome.grid(
            column=1, row=4,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.med_nome = tk.Entry(self.base.tela_)
        self.med_nome.grid(
            column=2, row=4, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='WE'
        )

        # Botão de Enviar
        self.bt_enviar = tk.Button(
            self.base.tela_,
            text='Enviar',
            command=self.enviar
        )
        self.bt_enviar.grid(column=4, row=100, sticky='E')

        # Botão Voltar
        self.bt_voltar = tk.Button(
            self.base.tela_,
            text="Voltar",
            command=self.voltar
        )
        self.bt_voltar.grid(column=1, row=100, sticky='W')

    def fechar_Médico(self, enviar: bool = False):
        self.info_médico.destroy()
        self.info_CRM.destroy()
        self.CRM.destroy()
        self.info_espec.destroy()
        self.espec.destroy()
        self.info_nome.destroy()
        self.med_nome.destroy()

        self.bt_enviar.destroy()
        self.bt_voltar.destroy()

        if not (self.val_erro):
            self.error_message.destroy()

        self.cria_Médico() if enviar else self.base.Menu_inicial.cria_Menu()

    def voltar(self):
        self.fechar_Médico()

    def enviar(self):
        self.medico_ = Médico(
            self.CRM.get(),
            self.espec.get(),
            self.med_nome.get()
        )

        if not ((self.medico_.crm == '') or (self.medico_.espec == '') or
                (self.medico_.nome == '')):

            self.base.Médicos.lista_médicos.append(self.medico_)

            # ----  ENVIAR MÉDICO  ---- #

            self.fechar_Médico(True)
        else:
            # Mostra erro
            if self.val_erro:  # val_error está disponível?
                print("Error - Nenhum valor inserido")
                self.error_message = tk.Label(
                    self.base.tela_,
                    text='Error - Numero de Recém Nascidos INVALIDO'
                )
                self.error_message.grid(column=5, row=10, sticky='E')
                self.val_erro = False


class Menu_do_Bebê():
    def __init__(self, parto: Menu_do_Parto) -> None:
        self.parto: Menu_do_Parto = parto
        self.base: Iniciar_sistema = self.parto.base

        self.médico: Médico = self.parto.parto.médico
        self.mãe: Mãe = self.parto.parto.mãe

        self.bebê: Bebê = Bebê(self.mãe, self.médico, self.parto)
        self.numero_do_bebe: int = 1

        self.voltando = False
        self.mensagem_erro = False

    def cadastrar_bebê(self):

        self.titulo = tk.Label(
            self.base.tela_,
            text=f"Insira o {len(self.mãe.lista_filhos)+1}° Bebê: ",
        )
        self.titulo.grid(
            column=1, row=0,
            padx=0.5, pady=0.5,
            sticky='E'
        )

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
            command=self.voltar
        )
        self.bt_voltar_parto.grid(column=1, row=10, sticky='W')

    def voltar(self):
        self.voltando = True
        self.fechar_bebê()

    def fechar_bebê(self):
        self.titulo.destroy()
        self.informe_nome.destroy()
        self.nome_bebê.destroy()
        self.informe_sexo.destroy()
        self.var_0.destroy()
        self.var_1.destroy()
        self.var_2.destroy()
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
        if self.mensagem_erro:
            self.mensagem_erro = False
            self.error_message_1.destroy()

        self.ver = len(self.mãe.lista_filhos) < int(self.mãe.num_filhos)
        if self.ver and not (self.voltando):
            self.parto.inserir_bebês()
        else:
            self.parto.cria_Parto()

    def enviar(self):
        if (self.nome_bebê.get() == '' or self.sexo_bebe.get() == '' or
            self.peso_bebê.get() == '' or self.altura_bebê.get() == '' or
            self.data_bebê.get() == '' or self.hora_bebê.get() == '' or
                self.pre_bebê.get() == '' or self.sob_bebê.get() == ''):
            print("Error - Preencha todos os campos")
            if not (self.mensagem_erro):
                self.error_message_1 = tk.Label(
                    self.base.tela_,
                    text='Error - Preencha todos os campos'
                )
                self.error_message_1.grid(column=5, row=10, sticky='E')
                self.mensagem_erro = True
            return

        self.mãe.lista_filhos.append(self)

        # ---- ENVIAR BEBE ---- #

        self.fechar_bebê()


Iniciar_sistema()
