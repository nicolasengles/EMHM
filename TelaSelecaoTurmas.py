import tkinter as tk
from PIL import Image, ImageTk

class TelaPerguntas(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        # Carrega e desenha o fundo
        raw_fundo = Image.open(r'images\black-solid-background-2920-x-1642-jk98dr7udfcq3hqj.jpg')\
            .resize((width, height), Image.LANCZOS)
        self.imagem_fundo = ImageTk.PhotoImage(raw_fundo)
        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)

        # Título do painel
        self.create_text(640, 100,
            text="Manutenção de Turmas",
            font=("Arial", 24, "bold"),
            fill="white",
            anchor='n'
        )
        # Instruções da tela
        self.create_text(640, 200,
            text="Selecione a turma que deseja editar ou excluir.",
            font=("Arial", 16),
            fill="white",
            anchor='n'
        )
        #Lista visual
        self.lista_perguntas = tk.Listbox(self, width=80, height=10, font=("Arial", 14))
        self.lista_perguntas.place(x=200, y=250)

        #Adicionar turmas de exemplo
        lista_perguntas = [
            "Turma A: História Antiga",
            "Turma B: História Medieval",
            "Turma C: História Moderna",
        ]
        
        for pergunta in lista_perguntas:
            self.lista_perguntas.insert(tk.END, pergunta)
        
        # Botão confirmar
        btn_confirmar_tag = 'btn_confirmar'
        self.create_text(1200, 690,
            text="CONFIRMAR",
            font=("Arial", 18, "bold"),
            fill="white",
            anchor='n',
            tags=(btn_confirmar_tag,)
        )

        # Botão voltar
        btn_voltar_tag = 'btn_voltar'
        self.create_text(60, 690,
            text="VOLTAR",
            font=("Arial", 18, "bold"),
            fill="white",
            anchor='n',
            tags=(btn_voltar_tag,)
        )
