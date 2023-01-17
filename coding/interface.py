import re
import tkinter as tk

from bancoDeDados import (BD_export_Admin, BD_export_Bb, BD_export_Mae,
                          BD_export_medico, BD_export_parto, BD_getInfo_adim,
                          BD_getInfo_medico, BD_GetMedico, BD_Valida_admin,
                          BD_Valida_CPF_Mae, BD_Valida_CRM_Medico,
                          encerrar_conexao)
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
        encerrar_conexao()

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
            self.tela_login()
        else:
            self.tela_login(True)

    def tela_login(self, cadastro=False):
        self.cadastro = cadastro

        if self.cadastro:
            self.primeiro = tk.Label(
                self.tela_,
                text="""Como não existem admins no sistema \n
                        Cadastre o principal"""
            )
            # self.login.place(relheight=0.1, relwidth=0.1)
            self.primeiro.grid(column=1, row=0, padx=2, pady=2)
        else:
            self.primeiro = tk.Label(
                self.tela_,
                text="""Tela de Login"""
            )
            # self.login.place(relheight=0.1, relwidth=0.1)
            self.primeiro.grid(column=1, row=0, padx=2, pady=2)

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

        if not (self.cadastro):
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

        if len(self.alter_cpf) < 11:
            self.erro_de_login('CPF invalido')
            return

        if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            self.alter_cpf = (cpf[0:3]+cpf[4:7] +
                              cpf[8:11]+cpf[12:14])  # 012.456.890-90

        self.user = Usuario(self.alter_cpf, self.senha_En.get())

        if BD_Valida_admin(self.user):
            self.deleta_login()
            self.Menu_inicial.cria_Menu()
        else:
            self.erro_de_login('Senha ou Login incorretos')
            return

    def cadastrar(self):
        cpf = self.cpf_En.get()
        self.alter_cpf = cpf
        if (cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'):
            self.alter_cpf = (cpf[0:3]+cpf[4:7]+cpf[8:11]+cpf[12:14])

        valida = len(self.alter_cpf) < 11
        if valida:
            self.erro_de_login('CPF invalido')
        else:
            print(self.alter_cpf)
            self.user = Usuario(self.alter_cpf, self.senha_En.get())

            if BD_Valida_admin(self.user, True):
                print('CPF Já está Cadastrado')
                self.erro_de_login('CPF Já está Cadastrado')
                return

            BD_export_Admin(self.user)
            self.deleta_login()
            self.tela_login()

    def erro_de_login(self, texto='ERROR'):
        if self.erro:
            self.er_senha.destroy()

        self.er_senha = tk.Label(
            self.tela_,
            text=f"""{texto}""",
            border=1,
            background='grey',
        )
        self.er_senha.grid(
            column=10, row=1,
            padx=2, pady=2,
            sticky='WE'
        )
        self.erro = True

    def deleta_login(self):
        self.primeiro.destroy()
        self.cpf.destroy()
        self.senha.destroy()
        self.cpf_En.destroy()
        self.senha_En.destroy()
        if self.erro:
            self.er_senha.destroy()

        self.bt1.destroy() if not (self.cadastro) else self.bt2.destroy()


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

        if not (BD_getInfo_medico()):
            self.bt_parto = tk.Button(
                self.base.tela_,
                text="Cadastrar Parto",
                state=tk.DISABLED
            )
            self.bt_parto.grid(column=2, row=1, padx=0.5, pady=0.5)
        else:
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
        self.parto: Parto = Parto()

        self.status_mãe: bool = False

        self.erro_mostrado: bool = False

        self.val_erro: bool = True

        self.enviado: bool = False

    def cria_Parto(self):

        self.status_mãe = False
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
            self.error_("Numero de Recém Nascidos INVALIDO")
            return

        if self.enviado and (self.cpf.get() == '' or
                             self.caixa_crm.get() == ''):
            self.error_("Insira o CPF da Mãe e/ou o CRM do Médico")
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
            self.error_message.destroy()

        if self.status_mãe:
            self.deleta_cadastrar_mãe()

        self.info_número_rn.destroy()
        self.número_rn.destroy()

        self.bt_voltar_parto.destroy()

        if not (self.enviado):
            self.base.Menu_inicial.cria_Menu()
        else:
            self.inserir_bebês()

    def error_(self, texto: str, x=10, y=10):
        self.error_message: tk.Label
        if self.erro_mostrado:
            self.error_message.destroy()
            self.erro_mostrado = False

        print(f"Error - {texto}")
        self.error_message = tk.Label(
            self.base.tela_,
            text=f'{texto}'
        )
        self.error_message.grid(column=x, row=y, sticky='E')

        self.erro_mostrado = True

    def inserir_bebês(self):
        bebe_temp = Menu_do_Bebê(self)
        bebe_temp.cadastrar_bebê()

    def enviar(self):
        self.enviado = True

        temp_med = Médico(crm=self.caixa_crm.get())
        if not (BD_Valida_CRM_Medico(temp_med)):
            self.error_("Médico não encontrado", 5, 1)
            return

        aux_crm, aux_nome = BD_GetMedico(temp_med.crm)

        self.parto.médico.crm = aux_crm
        self.parto.médico.nome = aux_nome

        cpf = self.cpf.get()
        self.alter_cpf = cpf

        if len(self.alter_cpf) < 11:
            self.error_('CPF invalido')
            return

        if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            self.alter_cpf = (cpf[0:3]+cpf[4:7] +
                              cpf[8:11]+cpf[12:14])  # 012.456.890-90

        self.parto.mãe.cpf = self.alter_cpf

        if not (self.valida.get()):
            if self.nome_mãe.get() == '' or self.data_n.get() == '':
                self.error_(
                    "Preencha os campos Nome e Data de Nascimento", 5, 3)
                return

            if not (re.match(r'\d{2}/\d{2}/\d{4}', self.data_n.get())):
                self.error_("Data Incorreta, tente dd/mm/aaaa", 5, 3)
                return

            temp_data = self.data_n.get()
            if int(temp_data[:2]) > 31 or int(temp_data[3:5]) > 12:
                self.error_("Data Incorreta, tente dd/mm/aaaa", 5, 3)
                return
            data_n = temp_data[6:] + "-" + \
                temp_data[3:5] + "-" + temp_data[:2]

            self.parto.mãe.nome = self.nome_mãe.get()
            self.parto.mãe.endereço = self.endereço.get()
            self.parto.mãe.telefone = self.telefone.get()
            print(data_n)
            self.parto.mãe.data_nasci = data_n

            try:
                int(self.número_rn.get())
            except ValueError:
                self.error_("Número de Filhos invalido", 5, 10)
                return

            self.parto.mãe.num_filhos = int(self.número_rn.get())

        elif not (BD_Valida_CPF_Mae(self.parto.mãe)):
            self.error_("Mãe não cadastrada", 5, 3)
            return

        self.fechar_Parto()


class Menu_do_Médico():
    def __init__(self, base: Iniciar_sistema) -> None:
        self.base = base
        self.val_erro: bool = False

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
            text="CRM/",
        )
        self.info_CRM.grid(
            column=1, row=2,
            padx=0.5, pady=0.5,
            sticky='E'
        )

        self.sigla = tk.Entry(self.base.tela_)
        self.sigla.grid(
            column=2, row=2,
            padx=0.5, pady=0.5,
            sticky='WE'
        )
        self.digitos = tk.Entry(self.base.tela_)
        self.digitos.grid(
            column=3, row=2, columnspan=3,
            padx=0.5, pady=0.5,
            sticky='W'
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
        self.bt_enviar.grid(column=4, row=10, sticky='E')

        # Botão Voltar
        self.bt_voltar = tk.Button(
            self.base.tela_,
            text="Voltar",
            command=self.voltar
        )
        self.bt_voltar.grid(column=1, row=10, sticky='W')

    def fechar_Médico(self, enviar: bool = False):
        self.info_médico.destroy()
        self.info_CRM.destroy()
        self.sigla.destroy()
        self.digitos.destroy()
        self.info_espec.destroy()
        self.espec.destroy()
        self.info_nome.destroy()
        self.med_nome.destroy()

        self.bt_enviar.destroy()
        self.bt_voltar.destroy()

        if self.val_erro:
            self.error_message.destroy()
            self.val_erro = False

        self.cria_Médico() if enviar else self.base.Menu_inicial.cria_Menu()

    def voltar(self):
        self.fechar_Médico()

    def valida_CRM(self, CRM: str):
        if CRM[4:6] == '' or CRM[6:] == '' or len(CRM) != 12:
            return False

        print(CRM[6:])
        try:
            int(CRM[6:])
        except ValueError:
            return False

        print(CRM[4:6])
        try:
            if int(CRM[5:7]):
                return False
        except ValueError:
            return True

        return True

    def enviar(self):
        crm = "CRM/" + self.sigla.get() + self.digitos.get()

        if ((self.sigla.get() == '') and (self.espec.get() == '') and
                (self.med_nome.get() == '')):
            self.error_("Nenhum valor inserido", 5, 10)
            return
        if not (self.valida_CRM(crm)):
            self.error_("Crm incorreto", 5, 2)
            return
        if self.med_nome.get() == '':
            self.error_("insira um nome ao médico", 5, 4)
            return

        self.medico_ = Médico(
            crm=crm,
            espec=self.espec.get(),
            nome=self.med_nome.get()
        )

        if BD_Valida_CRM_Medico(self.medico_):
            self.error_("Médico já cadastrado", 5, 10)
            return

        self.error_("Médico inserido com SUCESSO", 5, 10)

        BD_export_medico(self.medico_)

        self.fechar_Médico(True)

    def error_(self, texto: str, x=10, y=10):
        self.error_message: tk.Label
        # Mostra erro
        if self.val_erro:  # val_error está disponível?
            self.error_message.destroy()

        print(f"{texto}")
        self.error_message = tk.Label(
            self.base.tela_,
            text=f"{texto}"
        )
        self.error_message.grid(column=x, row=y, sticky='E')

        self.val_erro = True


class Menu_do_Bebê():
    def __init__(self, menu_parto: Menu_do_Parto) -> None:
        self.menu_parto = menu_parto
        self.parto: Parto = self.menu_parto.parto
        self.base: Iniciar_sistema = self.menu_parto.base

        self.médico: Médico = self.parto.médico
        self.mãe: Mãe = self.parto.mãe

        self.numero_do_bebe: int = 1

        self.error_message: tk.Label
        self.voltando = False
        self.val_erro = False

    def cadastrar_bebê(self):

        self.titulo = tk.Label(
            self.base.tela_,
            text="Insira o Bebê: ",
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
        if self.val_erro:
            self.val_erro = False
            self.error_message.destroy()

        self.ver = len(self.mãe.lista_filhos) < int(self.mãe.num_filhos)
        if self.ver and not (self.voltando):
            self.menu_parto.inserir_bebês()
        else:
            self.menu_parto.cria_Parto()

    def enviar(self):
        if (self.nome_bebê.get() == '' or self.sexo_bebe.get() == '' or
            self.peso_bebê.get() == '' or self.altura_bebê.get() == '' or
            self.data_bebê.get() == '' or self.hora_bebê.get() == '' or
                self.pre_bebê.get() == '' or self.sob_bebê.get() == ''):
            self.error_("Preencha todos os campos")
            return

        if not (re.match(r'\d{2}/\d{2}/\d{4}', self.data_bebê.get())):
            self.error_("Data Incorreta, tente dd/mm/aaaa", 5, 3)
            return
        else:
            temp_data = self.data_bebê.get()
            if int(temp_data[:2]) > 31 or int(temp_data[3:5]) > 12:
                self.error_("Data Incorreta, tente dd/mm/aaaa", 5, 3)
                return
            data_bebê = temp_data[6:] + "-" + \
                temp_data[3:5] + "-" + temp_data[:2]

        if not (re.match(r'\d{2}:\d{2}', self.hora_bebê.get())):
            self.error_("Data Incorreta, tente hh:mm", 5, 3)
            return
        else:
            temp_hora = self.hora_bebê.get()
            if (int(temp_hora[:2]) > 24 or int(temp_hora[3:5]) > 59):
                self.error_("Data Incorreta, tente hh:mm", 5, 3)
                return
            hora_bebê = temp_hora[:2]+temp_hora[3:5]

        try:
            float(self.peso_bebê.get())
        except ValueError:
            self.error_("Insira um Peso Válido", 5, 4)
            return

        try:
            float(self.altura_bebê.get())
        except ValueError:
            self.error_("Insira uma Altura Válida", 5, 5)
            return

        d_cpf = self.mãe.cpf[:5]  # 5 dígitos
        n_data = data_bebê[5:7] + data_bebê[8:]  # 4 dígitos

        self.parto.cod_parto = d_cpf + n_data
        self.parto.data_n = data_bebê

        self.bebê = Bebê(self.mãe, self.médico, self.parto)

        if not (BD_Valida_CPF_Mae(self.mãe)):
            BD_export_Mae(self.mãe)
            BD_export_parto(self.parto)

        self.bebê.nome = self.nome_bebê.get()
        self.bebê.sexo = self.sexo_bebe.get()
        self.bebê.peso = float(self.peso_bebê.get())
        self.bebê.altura = float(self.altura_bebê.get())
        self.bebê.data_nasci = data_bebê
        self.bebê.hora_nasci = hora_bebê
        self.bebê.prematuro = self.pre_bebê.get()
        self.bebê.sobrevive = self.sob_bebê.get()

        BD_export_Bb(self.bebê)

        self.fechar_bebê()

    def error_(self, text: str, x=10, y=10):
        print(f"Error - {text}")
        if self.val_erro:
            self.error_message.destroy()

        self.error_message = tk.Label(
            self.base.tela_,
            text=f"{text}"
        )
        self.error_message.grid(column=x, row=y, sticky='E')


Iniciar_sistema()
