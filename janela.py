import tkinter as tk
from TelaMenuPrincipal import *
<<<<<<< HEAD
from TelaInicial import *
from TelaPartida import * 
from TelaGameOver import *
from TelaLoginProfessor import *
from DbManagement import *
from TelaSelecaoPerguntas import *
=======
# from TelaInicial import *
# from TelaPartida import * 
# from TelaGameOver import *
# from TelaLoginProfessor import *
# from DbManagement import *
>>>>>>> 412c48e6c217ada96bd626d32b02e789e86ccb3d

class Janela():
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Expedição do Milhão: Histórias e Mapas')
        self.janela.minsize(1280, 720)
        self.janela.maxsize(1280, 720)

<<<<<<< HEAD
    #  Definir tela_atual aqui:
    tela_atual = TelaSelecaoPerguntas(master=janela)
=======
        #  Definir tela_atual aqui:
        self.tela_atual = TelaMenuPrincipal(master=self.janela)
>>>>>>> 412c48e6c217ada96bd626d32b02e789e86ccb3d

    def iniciar_janela(self):
        self.janela.mainloop()

    def mudar_tela(self, tela_nova):
        self.tela_atual.destroy()
        self.tela_atual = tela_nova

janela = Janela()
