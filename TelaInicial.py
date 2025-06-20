import tkinter as tk
from PIL import Image, ImageTk
import janela
from TelaInicialProfessor import TelaInicialProfessor
from TelaLoginAluno import TelaLoginAluno

class TelaInicial(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        img_fundo = Image.open('images/imagemfundo0.png')
        self.imagem_fundo = ImageTk.PhotoImage(img_fundo)

        raw_alt = Image.open('images/Alternativa.png').resize((330, 62), Image.LANCZOS)
        self.imagem_alt = ImageTk.PhotoImage(raw_alt)

        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)

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

        self.create_text(640, 300,
            text="Como Deseja Prosseguir?",
            font=("Sylfaen", 32, "bold"),
            fill="black",
            anchor='n'
        )

        btn_aluno_tag = 'btn_aluno'
        self.create_image(
            640, 400,
            image=self.imagem_alt,
            anchor='n',
            tags=(btn_aluno_tag,)
        )
        self.create_text(640, 415,
            text="ALUNO",
            font=("Sylfaen", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_aluno_tag)
        )
        self.tag_bind(btn_aluno_tag, '<Button-1>', lambda event: janela.janela.mudar_tela(TelaLoginAluno))

        btn_prof_tag = 'btn_professor'
        self.create_image(
            640, 500,
            image=self.imagem_alt,
            anchor='n',
            tags=(btn_prof_tag)
        )
        self.create_text(640, 515,
            text="PROFESSOR",
            font=("Sylfaen", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_prof_tag)
        )
        self.tag_bind(btn_prof_tag, '<Button-1>', lambda event: janela.janela.mudar_tela(TelaInicialProfessor))         
