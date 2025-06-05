import tkinter as tk
from PIL import Image, ImageTk
import janela
from app import app

class TelaIniciarPartida(tk.Canvas):
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
        raw_btn = Image.open('images/Alternativa.png')\
                         .resize((330, 62), Image.LANCZOS)
        self.imagem_btn = ImageTk.PhotoImage(raw_btn)

        self.create_image(0, 0, image=self.imagem_fundo, anchor='nw')
        self.create_image(640, 100, image=self.imagem_titulo, anchor='n')
        self.create_image(810, 200, image=self.imagem_subtitulo, anchor='n')

        btn_hist_tag = 'btn_historia'
        self.create_image(640, 300,
            image=self.imagem_btn,
            anchor='n',
            tags=(btn_hist_tag)
        )
        self.create_text(640, 315,
            text="HISTÓRIA",
            font=("Californian FB", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_hist_tag)
        )       
        self.tag_bind(btn_hist_tag, '<Button-1>', lambda event: self.jogar(event, 0))

        btn_geo_tag = 'btn_geografia'
        self.create_image(640, 400,
            image=self.imagem_btn,
            anchor='n',
            tags=(btn_geo_tag)
        )
        self.create_text(640, 415,
            text="GEOGRAFIA",
            font=("Californian FB", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_geo_tag)
        ) 
        self.tag_bind(btn_geo_tag, '<Button-1>', lambda event: self.jogar(event, 1))

        btn_amb_tag = 'btn_ambas'
        self.create_image(640, 500,
            image=self.imagem_btn,
            anchor='n',
            tags=(btn_amb_tag)
        )
        self.create_text(640, 515,
            text="HISTÓRIA E GEOGRAFIA",
            font=("Californian FB", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_amb_tag)
        )
        self.tag_bind(btn_amb_tag, '<Button-1>', lambda event: self.jogar(event, 2))

        btn_amb_tag = 'btn_voltar'
        self.create_image(640, 600,
            image=self.imagem_btn,
            anchor='n',
            tags=(btn_amb_tag)
        )
        self.create_text(640, 615,
            text="VOLTAR",
            font=("Californian FB", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_amb_tag)
        )
        self.tag_bind(btn_amb_tag, '<Button-1>', self.voltar)

    def jogar(self, event=None, materia=None):
        app.iniciar_partida(materia=materia)

    def voltar(self, event):
        from TelaMenuPrincipal import TelaMenuPrincipal
        janela.janela.mudar_tela(TelaMenuPrincipal)
