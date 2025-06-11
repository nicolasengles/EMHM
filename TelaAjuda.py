import tkinter as tk
from PIL import Image, ImageTk
import janela
import partida
import app

class TelaAjuda(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        img_fundo = Image.open('images/imagemfundo0.png')
        self.imagem_fundo = ImageTk.PhotoImage(img_fundo)

        raw_alt = Image.open('images/Alternativa.png').resize((330, 62), Image.LANCZOS)
        self.imagem_alt = ImageTk.PhotoImage(raw_alt)
        
        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)

        self.create_text(640, 150,
            text="AJUDAS",
            font=("Sylfaen", 48, "bold"),
            fill="black",
            anchor='n'
        )

        if partida.Ajuda.DICA in app.app.partida.ajudas_disponiveis:
            btn_tag = 'btn_dica'
            self.create_image(640, 250, image=self.imagem_alt, anchor='n', tags=(btn_tag))
            self.create_text(640, 280,
                text="DICA",
                font=("Sylfaen", 28, "bold"),
                tags=(btn_tag)
            )
            self.tag_bind(btn_tag, '<Button-1>', self._on_ajuda_dica)
            self.tag_bind(btn_tag, '<Button-1>', self._on_ajuda_dica)

        if partida.Ajuda.DUAS_OPCOES in app.app.partida.ajudas_disponiveis:
            btn_tag = 'btn_duas_opcoes'
            self.create_image(640, 350, image=self.imagem_alt, anchor='n', tags=(btn_tag))
            self.create_text(640, 380,
                text="DUAS OPÇÕES",
                font=("Sylfaen", 28, "bold"),
                tags=(btn_tag)
            )
            self.tag_bind(btn_tag, '<Button-1>', self._on_ajuda_remover_duas)
            self.tag_bind(btn_tag, '<Button-1>', self._on_ajuda_remover_duas)

        if partida.Ajuda.PLATEIA in app.app.partida.ajudas_disponiveis:
            btn_tag = 'btn_plateia'
            self.create_image(640, 450, image=self.imagem_alt, anchor='n', tags=(btn_tag))
            self.create_text(640, 480,
                text="PLATEIA",
                font=("Sylfaen", 28, "bold"),
                tags=(btn_tag)
            )
            self.tag_bind(btn_tag, '<Button-1>', self._on_ajuda_plateia)
            self.tag_bind(btn_tag, '<Button-1>', self._on_ajuda_plateia)

        btn_tag = 'btn_voltar'
        self.create_image(640, 550, image=self.imagem_alt, anchor='n', tags=(btn_tag))
        self.create_text(640, 580,
            text="VOLTAR",
            font=("Sylfaen", 28, "bold"),
            fill="darkred",
            tags=(btn_tag)
        )
        self.tag_bind(btn_tag, '<Button-1>', self.voltar)
        self.tag_bind(btn_tag, '<Button-1>', self.voltar)

    def _on_ajuda_dica(self, event):
        app.app.partida.utilizar_ajuda(partida.Ajuda.DICA)

    def _on_ajuda_remover_duas(self, event):
        app.app.partida.utilizar_ajuda(partida.Ajuda.DUAS_OPCOES)

    def _on_ajuda_plateia(self, event):
        app.app.partida.utilizar_ajuda(partida.Ajuda.PLATEIA)

    def voltar(self, event):
        app.app.partida.exibir_tela_partida()