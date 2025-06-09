import tkinter as tk
from PIL import Image, ImageTk
from sgbd import autenticar_usuario
import janela
import TelaInicial
from TelaLoginProfessor import TelaLoginProfessor
from TelaCadastroProfessor import TelaCadastroProfessor

class TelaInicialProfessor(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        raw_fundo = Image.open(r'images/black-solid-background-2920-x-1642-jk98dr7udfcq3hqj.jpg')\
            .resize((width, height), Image.LANCZOS)
        
        self.imagem_fundo = ImageTk.PhotoImage(raw_fundo)
        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)

        self.create_text(640, 200,
            text="PAINEL DO PROFESSOR",
            font=("Arial", 24, "bold"),
            fill="white",
            anchor='n'
        )

        self.create_text(640, 250,
            text="Como deseja prosseguir?",
            font=("Arial", 18),
            fill="white",
            anchor='n'
        )

        btn_login_tag = 'btn_login'
        self.create_text(640, 325,
            text="FAZER LOGIN",
            font=("Arial", 18, "bold"),
            fill="white",
            anchor='n',
            tags=(btn_login_tag)
        )
        self.tag_bind(btn_login_tag, '<Button-1>', lambda event: janela.janela.mudar_tela(TelaLoginProfessor))

        btn_cadastro_tag = 'btn_cadastro'
        self.create_text(640, 400,
            text="FAZER CADASTRO",
            font=("Arial", 18, "bold"),
            fill="white",
            anchor='n',
            tags=(btn_cadastro_tag)
        )
        self.tag_bind(btn_cadastro_tag, '<Button-1>', lambda event: janela.janela.mudar_tela(TelaCadastroProfessor))

        btn_sair_tag = 'btn_sair'
        self.create_text(640, 475,
            text="VOLTAR",
            font=("Arial", 18, "bold"),
            fill="red",
            anchor='n',
            tags=(btn_sair_tag)
        )
        self.tag_bind(btn_sair_tag, '<Button-1>', self.voltar)

    def voltar(self, event):
        janela.janela.mudar_tela(TelaInicial.TelaInicial)
