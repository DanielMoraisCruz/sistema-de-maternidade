import tkinter as tk


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
            command=self.fechar_Parto
        )
        self.bt_voltar_parto.grid(column=1, row=10, sticky='W')

    def fechar_Parto(self):
        self.info_médico.destroy()
        self.caixa_crm.destroy()
        self.info_mãe.destroy()
        self.bt_enviar.destroy()
        self.var_0.destroy()
        self.var_1.destroy()
        self.info_cpf.destroy()
        self.cpf.destroy()

        if self.status_mãe:
            self.deleta_cadastrar_mãe()

        self.info_número_rn.destroy()
        self.número_rn.destroy()

        self.bt_voltar_parto.destroy()
        self.base.Menu_inicial.cria_Menu()

    def enviar(self):
        print("CRN:", self.caixa_crm.get())
        print("Mãe cadastrada?:", self.valida.get())

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


Iniciar_sistema()
