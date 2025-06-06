import tkinter as tk
from PIL import Image, ImageTk
import janela
import app

class TelaPerfil(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        img = Image.open('images/imagemfundo0.png')
        self.imagem_fundo = ImageTk.PhotoImage(img)
        raw_alt = Image.open('images/Alternativa.png').resize((330, 62), Image.LANCZOS)
        self.imagem_alt = ImageTk.PhotoImage(raw_alt)

        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)
        self.create_text(640, 100,
            text="PERFIL",
            font=("Californian FB", 48, "bold"),
            fill="darkred",
            anchor='n'
        )
        
        self.create_text(640, 200,
            text="Nome: " + app.app.usuario.nome,
            font=("Californian FB", 30, "bold"),
            fill="black",
            anchor='n'
        )

        self.create_text(640, 300,
            text="Email: " + app.app.usuario.email,
            font=("Californian FB", 30, "bold"),
            fill="black",
            anchor='n'
        )

        self.create_text(640, 400,
            text="Turma: " + app.app.usuario.turma.nome,
            font=("Californian FB", 30, "bold"),
            fill="black",
            anchor='n'
        )

        self.create_text(640, 500,
            text="Conta Bancária: R$" + str(app.app.usuario.pontuacao),
            font=("Californian FB", 30, "bold"),
            fill="black",
            anchor='n'
        )

        btn_tag = 'btn_voltar'
        self.create_image(640, 600,
            image=self.imagem_alt,
            anchor='n',
            tags=(btn_tag,)
        )
        self.create_text(640, 615,
            text="VOLTAR",
            font=("Californian FB", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_tag,)
        )
        self.tag_bind(btn_tag, '<Button-1>', self.voltar)

    def voltar(self, event):
        from TelaMenuPrincipal import TelaMenuPrincipal
        janela.janela.mudar_tela(TelaMenuPrincipal)
