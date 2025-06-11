import tkinter as tk
from PIL import Image, ImageTk
import janela
from app import app

class TelaIniciarPartida(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)
        
        img_fundo = Image.open('images/imagemfundo0.png')
        self.imagem_fundo = ImageTk.PhotoImage(img_fundo)

        raw_btn = Image.open('images/Alternativa.png').resize((330, 62), Image.LANCZOS)
        self.imagem_btn = ImageTk.PhotoImage(raw_btn)

        self.create_image(0, 0, image=self.imagem_fundo, anchor='nw')

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

        btn_hist_tag = 'btn_historia'
        self.create_image(640, 300,
            image=self.imagem_btn,
            anchor='n',
            tags=(btn_hist_tag)
        )
        self.create_text(640, 315,
            text="HISTÓRIA",
            font=("Sylfaen", 20, "bold"),
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
            font=("Sylfaen", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_geo_tag)
        ) 
        self.tag_bind(btn_geo_tag, '<Button-1>', lambda event: self.jogar(event, 1))

        (btn_todas_tag) = 'btn_todas'
        self.create_image(640, 500,
            image=self.imagem_btn,
            anchor='n',
            tags=((btn_todas_tag))
        )
        self.create_text(640, 515,
            text="TODAS",
            font=("Sylfaen", 20, "bold"),
            fill="black",
            anchor='n',
            tags=((btn_todas_tag))
        )
        self.tag_bind((btn_todas_tag), '<Button-1>', lambda event: self.jogar(event, 2))

        (btn_todas_tag) = 'btn_voltar'
        self.create_image(640, 600,
            image=self.imagem_btn,
            anchor='n',
            tags=((btn_todas_tag))
        )
        self.create_text(640, 615,
            text="VOLTAR",
            font=("Sylfaen", 20, "bold"),
            fill="black",
            anchor='n',
            tags=((btn_todas_tag))
        )
        self.tag_bind((btn_todas_tag), '<Button-1>', self.voltar)

        btn_mute_tag = 'btn_mute'
        self.create_text(1200, 660,
            text="DESATIVAR MÚSICA",
            font=("Sylfaen", 15, "bold"),
            fill="black",
            anchor='n',
            width=200,
            tags=(btn_mute_tag,),
            justify='center'
        )
        # binding corrigido:
        self.tag_bind(
            btn_mute_tag, '<Button-1>',
            lambda e: janela.janela.toggle_mute(self, btn_mute_tag)
        )

    def jogar(self, event=None, materia=None):
        app.iniciar_partida(materia=materia)

    def voltar(self, event):
        from TelaMenuPrincipal import TelaMenuPrincipal
        janela.janela.mudar_tela(TelaMenuPrincipal)
