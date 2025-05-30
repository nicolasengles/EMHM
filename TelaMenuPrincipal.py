import tkinter as tk
from PIL import Image, ImageTk
import janela
from TelaPartida import *

class TelaMenuPrincipal(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master)
        # Carregar imagens
        imagem_fundo         = tk.PhotoImage(file='images/imagemfundo0.png')
        arquivo_imagem_titulo      = Image.open(r"images/EXPEDICAO_DO_MILHAO.png").resize((750, 75), Image.LANCZOS)
        imagem_titulo      = ImageTk.PhotoImage(arquivo_imagem_titulo)
        arquivo_imagem_botao1 = Image.open(r"images/Frame.png").resize((300, 80), Image.LANCZOS)
        imagem_botao1     = ImageTk.PhotoImage(arquivo_imagem_botao1)
        arquivo_imagem_botao2 = Image.open(r"images/Frame_3.png").resize((203,58), Image.LANCZOS)
        imagem_botao2   = ImageTk.PhotoImage(arquivo_imagem_botao2)
        arquivo_imagem_subtitulo    = Image.open(r"images/HistoriaseMapas.png").resize((500, 65), Image.LANCZOS)
        imagem_subtitulo      = ImageTk.PhotoImage(arquivo_imagem_subtitulo)
        # Criar canvas e adicionar título, subtitulo e imagem de fundo
        self.pack(fill="both", expand=True)
        self.create_image(0, 0, image=imagem_fundo, anchor=tk.NW)
        self.create_image(640, 100, image=imagem_titulo, anchor='n')
        self.create_image(810, 200, image=imagem_subtitulo)
        # Botão jogar
        botao_x, botao_y = 640, 300 + 62 + 15
        comprimento_botao, altura_botao = 406, 70

        retangulo1 = self.create_rectangle(
            botao_x - comprimento_botao/2, botao_y,
            botao_x + comprimento_botao/2, botao_y + altura_botao,
            fill='', outline=''
        )
        imagem1 = self.create_image(botao_x, botao_y, image=imagem_botao1, anchor='n')

        def on_first_click(event):
            janela.Janela.mudar_tela(tela_nova=TelaPartida)

        for tag in (retangulo1, imagem1):
            self.tag_bind(tag, '<Button-1>', on_first_click)

        # Segundo botão
        botao2_y = botao_y + altura_botao + 30
        retangulo2 = self.create_rectangle(
            botao_x - comprimento_botao/2, botao2_y,
            botao_x + comprimento_botao/2, botao2_y + altura_botao,
            fill='', outline=''
        )
        imagem2 = self.create_image(botao_x, botao2_y, image=imagem_botao2, anchor='n')

        def on_second_click(event):
            print("Segundo botão clicado")

        for tag in (retangulo2, imagem2):
            self.tag_bind(tag, '<Button-1>', on_second_click)

        # Manter imagens na memória
        master.bg_img = imagem_fundo
        master.title_img = imagem_titulo
        master.button_img = imagem_botao1
        master.subtitulo = imagem_subtitulo
