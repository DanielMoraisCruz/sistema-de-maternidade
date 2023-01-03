"""

Menu Inicial
    forma de inserir os dados de
        mãe
        bebê
        médico
    forma de solicitar esses dados
        crianças nascidas em um determinado período de tempo
        mães cadastradas
        médicos disponíveis

"""
import tkinter as tk


class Sistema_maternidade():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.config()

        self.menu_inicial = Menu(self.root)

        self.root.mainloop()

    def config(self):
        self.root.title("MATERNIDADE MARIA")
        self.root.config(background='lightblue')
        self.root.geometry("800x400")
        self.root.resizable(False, False)


class Menu():
    def __init__(self, root: tk.Tk) -> None:
        self.root: tk.Tk = root
        self.menu = tk.Frame(self.root)
        self.menu.place(relx=0.02, rely=0.02,
                        relwidth=0.96, relheight=0.96)

        self.botão_voltar()

    def desligar_menu(self):
        self.menu.destroy()

    def botão_voltar(self):
        self.bt = tk.Button(self.menu, 'Voltar')
        self.bt.place(
            relx=0.02, rely=0.02,
            relwidth=0.96, relheight=0.96
        )


Sistema_maternidade()
