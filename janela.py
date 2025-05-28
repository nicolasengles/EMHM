import tkinter as tk
from TelaMenuPrincipal import *

class Janela:
    #  Criar Janela
    janela = tk.Tk()
    janela.title('Expedição do Milhão: Histórias e Mapas')
    janela.minsize(1280, 720)
    janela.maxsize(1280, 720)

    #  Definir tela_atual aqui:
    tela_atual = TelaMenuPrincipal(master=janela)

    @staticmethod
    def iniciar_janela():
        Janela.janela.mainloop()

    @staticmethod
    def mudar_tela(tela_nova):
        Janela.tela_atual.destroy()
        Janela.tela_atual = tela_nova(master=Janela.janela)

