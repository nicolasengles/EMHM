import tkinter as tk
from PIL import Image, ImageTk
from TelaIniciarPartida import TelaIniciarPartida
from TelaPerfil import TelaPerfil
import janela

class TelaMenuPrincipal(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        self.imagem_fundo = tk.PhotoImage(file='images/imagemfundo0.png')
        raw_titulo = Image.open("images/EXPEDICAO_DO_MILHAO.png")\
                          .resize((750, 75), Image.LANCZOS)
        self.imagem_titulo = ImageTk.PhotoImage(raw_titulo)
        raw_sub = Image.open("images/HistoriaseMapas.png")\
                       .resize((500, 65), Image.LANCZOS)
        self.imagem_subtitulo = ImageTk.PhotoImage(raw_sub)
        raw_jogar = Image.open('images/Alternativa.png')\
                         .resize((330, 62), Image.LANCZOS)
        self.imagem_jogar = ImageTk.PhotoImage(raw_jogar)

        self.create_image(0, 0, image=self.imagem_fundo, anchor='nw')
        # self.create_image(640, 100, image=self.imagem_titulo, anchor='n')
        # self.create_image(810, 200, image=self.imagem_subtitulo, anchor='n')

        self.create_text(640, 100,
            text="EXPEDIÇÃO DO MILHÃO",
            font=("Sylfaen", 48, "bold"),
            fill="darkred",
            anchor='n'
        )

        self.create_text(775, 160,
            text="Histórias e Mapas",
            font=("Sylfaen", 48),
            fill="darkred",
            anchor='n'
        )

        btn_tag = 'btn_jogar'
        self.create_image(640, 350,
            image=self.imagem_jogar,
            anchor='n',
            tags=(btn_tag,)
        )

        self.create_text(640, 362,
            text="JOGAR",
            font=("Sylfaen", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_tag,)
        )   
        self.tag_bind(btn_tag, '<Button-1>', self.jogar)

        btn_tag = 'btn_perfil'
        self.create_image(640, 450,
            image=self.imagem_jogar,
            anchor='n',
            tags=(btn_tag,)
        )

        self.create_text(640, 462,
            text="PERFIL",
            font=("Sylfaen", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_tag,)
        )   
        self.tag_bind(btn_tag, '<Button-1>', self.perfil)

    def jogar(self, event):
        janela.janela.mudar_tela(TelaIniciarPartida)

    def perfil(self, event):
        janela.janela.mudar_tela(TelaPerfil)
