import tkinter as tk
from TelaMenuPrincipal import *

class EMHM:
    tela_atual = None
    janela = None

    def __init__(self):
        #  Criar Janela
        janela = tk.Tk()
        janela.title('Expedição do Milhão: Histórias e Mapas')
        janela.minsize(1280, 720)
        janela.maxsize(1280, 720)

        #  Definir tela_atual aqui:
        tela_atual = TelaMenuPrincipal(master=janela)

        #  NÃO MEXER NISSO
        janela.mainloop()

    @staticmethod
    def mudar_tela(janela, tela_nova):
        # tela_atual.destroy()
        tela_atual = tela_nova(master=janela)
        
# def main():
#     emhm = EMHM()

if __name__ == "__main__":
    emhm = EMHM()
