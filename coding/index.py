import tkinter as tk


class Iniciar_sistema():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.tela()
        self.frames_da_tela()

        self.menu = [1, 0, 0, 0]
        self.gerenciador_de_frames()
        self.root.mainloop()

    def tela(self):
        self.root.title("Menu Inicial")
        self.root.geometry("700x500")
        self.root.config(background='lightblue')

    def frames_da_tela(self):
        self.frame_1 = tk.Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = tk.Frame()
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def gerenciador_de_frames(self):
        print(self.menu)
        if self.menu[0]:
            self.menu_inicial()
        elif self.menu[1]:
            self.limpar_menu()
            self.cadastrar_mãe()
        elif self.menu[2]:
            self.limpar_menu()
            self.cadastrar_bebê()
        elif self.menu[3]:
            self.limpar_menu()
            self.cadastrar_médico()
        else:
            print("Erro de Validação de janelas")

    def menu_inicial(self):

        self.menu = [1, 0, 0, 0]

        self.intro = tk.Label(
            self.frame_1,
            text="Selecione a Opção de Cadastro",
            justify='left'
        )
        self.intro.place(relx=0.01, rely=0.1, relwidth=0.3, relheight=0.1)

        # Botão cadastrar Mãe
        self.bt_mãe = tk.Button(
            self.frame_1,
            text="Cadastrar Mãe",
            command=self.mudar_para_mãe
        )
        self.bt_mãe.place(relx=0.05, rely=0.3, relwidth=0.15, relheight=0.1)

        # Botão cadastrar Bebê
        self.bt_bebê = tk.Button(
            self.frame_1,
            text="Cadastrar Bebê",
            command=self.mudar_para_bebê
        )
        self.bt_bebê.place(relx=0.05, rely=0.45, relwidth=0.15, relheight=0.1)

        # Botão cadastrar Médico
        self.bt_médico = tk.Button(
            self.frame_1,
            text="Cadastrar Médico",
            command=self.mudar_para_médico
        )
        self.bt_médico.place(relx=0.05, rely=0.6,
                             relwidth=0.15, relheight=0.1)

    def cadastrar_mãe(self):
        self.intro = tk.Label(
            self.frame_1,
            text="Cadastre a mãe",
            justify='left'
        )
        self.intro.place(relx=0.01, rely=0.1, relwidth=0.3, relheight=0.1)

        # Botão Voltar
        self.bt_voltar_mãe = tk.Button(
            self.frame_2,
            text="Voltar",
            command=self.limpar_mãe
        )
        self.bt_voltar_mãe.place(relx=0.83, rely=0.85,
                                 relwidth=0.15, relheight=0.1)

    def cadastrar_bebê(self):
        self.intro = tk.Label(
            self.frame_1,
            text="Cadastre o bebê",
            justify='left'
        )
        self.intro.place(relx=0.01, rely=0.1, relwidth=0.3, relheight=0.1)

        # Botão Voltar
        self.bt_voltar_bebê = tk.Button(
            self.frame_2,
            text="Voltar",
            command=self.limpar_bebê
        )
        self.bt_voltar_bebê.place(relx=0.83, rely=0.85,
                                  relwidth=0.15, relheight=0.1)

    def cadastrar_médico(self):
        self.intro = tk.Label(
            self.frame_1,
            text="Cadastre o médico",
            justify='left'
        )
        self.intro.place(relx=0.01, rely=0.1, relwidth=0.3, relheight=0.1)

        # Botão Voltar
        self.bt_voltar_médico = tk.Button(
            self.frame_2,
            text="Voltar",
            command=self.limpar_médico
        )
        self.bt_voltar_médico.place(relx=0.83, rely=0.85,
                                    relwidth=0.15, relheight=0.1)

    def limpar_mãe(self):
        self.menu = [1, 0, 0, 0]
        self.bt_voltar_mãe.destroy()
        self.gerenciador_de_frames()

    def limpar_bebê(self):
        self.menu = [1, 0, 0, 0]
        self.bt_voltar_bebê.destroy()
        self.gerenciador_de_frames()

    def limpar_médico(self):
        self.menu = [1, 0, 0, 0]
        self.bt_voltar_médico.destroy()
        self.gerenciador_de_frames()

    def limpar_menu(self):
        self.intro.destroy()
        self.bt_mãe.destroy()
        self.bt_bebê.destroy()
        self.bt_médico.destroy()

    def mudar_para_mãe(self):
        print("cadastra mãe")
        self.menu = [0, 1, 0, 0]
        self.gerenciador_de_frames()

    def mudar_para_bebê(self):
        print("cadastra bebê")
        self.menu = [0, 0, 1, 0]
        self.gerenciador_de_frames()

    def mudar_para_médico(self):
        print("cadastra médico")
        self.menu = [0, 0, 0, 1]
        self.gerenciador_de_frames()


Iniciar_sistema()
