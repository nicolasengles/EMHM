    # AVISO: ESTE ARQUIVO SERVE SOMENTE COMO TEMPLATE PARA CRIAR OUTROS ARQUIVOS

    # NÃO IMPORTAR ESTE ARQUIVO EM NENHUM OUTRO

#  Importe aqui quaisquer outros módulos necessários, incluindo os de outras telas para a função "trocar_tela()"
import tkinter as tk

class TelaTemplate(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master)

        #  Insira aqui todo o código desta tela