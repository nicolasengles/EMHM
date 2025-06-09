import tkinter as tk
from TelaInicial import TelaInicial

class Janela():
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Expedição do Milhão: Histórias e Mapas')
        self.janela.minsize(1280, 720)
        self.janela.maxsize(1280, 720)

        #  Definir tela_atual aqui:
        self.tela_atual = TelaInicial(master=self.janela)

    def iniciar_janela(self):
        self.janela.mainloop()

    def mudar_tela(self, tela_nova):
        self.tela_atual.destroy()
        self.tela_atual = tela_nova(self.janela)

janela = Janela()
