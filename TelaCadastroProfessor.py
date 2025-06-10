import tkinter as tk
from PIL import Image, ImageTk
from sgbd import cadastrar_professor
import janela
import TelaInicialProfessor
from TelaPrincipalPainel import TelaPrincipalPainel

class TelaCadastroProfessor(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        raw_fundo = Image.open(r'images/black-solid-background-2920-x-1642-jk98dr7udfcq3hqj.jpg')\
            .resize((width, height), Image.LANCZOS)
        
        self.imagem_fundo = ImageTk.PhotoImage(raw_fundo)
        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)

        self.create_text(640, 250,
            text="PAINEL DO PROFESSOR",
            font=("Arial", 24, "bold"),
            fill="white",
            anchor='n'
        )

        placeholder_nome = "Digite seu nome:"
        entry_nome = tk.Entry(self, font=("Arial", 16), fg="gray")
        entry_nome.insert(0, placeholder_nome)
        self.create_window(640, 320, window=entry_nome, anchor='n', width=500)

        def on_focus_in_nome(event):
            if entry_nome.get() == placeholder_nome:
                entry_nome.delete(0, tk.END)
                entry_nome.config(fg="black")

        def on_focus_out_nome(event):
            if entry_nome.get().strip() == "":
                entry_nome.insert(0, placeholder_nome)
                entry_nome.config(fg="gray")

        entry_nome.bind("<FocusIn>", on_focus_in_nome)
        entry_nome.bind("<FocusOut>", on_focus_out_nome)

        placeholder_email = "Digite seu Email (@sistemapoliedro.com):"
        entry_email = tk.Entry(self, font=("Arial", 16), fg="gray")
        entry_email.insert(0, placeholder_email)
        self.create_window(640, 370, window=entry_email, anchor='n', width=500)

        def on_focus_in_email(event):
            if entry_email.get() == placeholder_email:
                entry_email.delete(0, tk.END)
                entry_email.config(fg="black")

        def on_focus_out_email(event):
            if entry_email.get().strip() == "":
                entry_email.insert(0, placeholder_email)
                entry_email.config(fg="gray")

        entry_email.bind("<FocusIn>", on_focus_in_email)
        entry_email.bind("<FocusOut>", on_focus_out_email)

        placeholder_senha = "Digite sua senha:"
        entry_senha = tk.Entry(self, font=("Arial", 16), fg="gray", show='*')
        entry_senha.insert(0, placeholder_senha)
        self.create_window(640, 420, window=entry_senha, anchor='n', width=500)

        def on_focus_in_senha(event):
            if entry_senha.get() == placeholder_senha:
                entry_senha.delete(0, tk.END)
                entry_senha.config(fg="black")

        def on_focus_out_senha(event):
            if entry_senha.get().strip() == "":
                entry_senha.insert(0, placeholder_senha)
                entry_senha.config(fg="gray")

        entry_senha.bind("<FocusIn>", on_focus_in_senha)
        entry_senha.bind("<FocusOut>", on_focus_out_senha)

        btn_cadastrar_tag = 'btn_cadastrar'
        self.create_text(640, 485,
            text="FAZER CADASTRO",
            font=("Arial", 18, "bold"),
            fill="light green",
            anchor='n',
            tags=(btn_cadastrar_tag)
        )
        self.tag_bind(btn_cadastrar_tag, '<Button-1>', lambda event: self.cadastrar(entry_nome.get(), entry_email.get(), entry_senha.get()))

        btn_sair_tag = 'btn_sair'
        self.create_text(640, 520,
            text="SAIR",
            font=("Arial", 18, "bold"),
            fill="red",
            anchor='n',
            tags=(btn_sair_tag)
        )
        self.tag_bind(btn_sair_tag, '<Button-1>', self.voltar)

        self.text_error = self.create_text(640, 460,
                text="",
                font=("Californian FB", 12, "bold"),
                fill="red",
                anchor='n'
            )

    def cadastrar(self, nome : str, email : str, senha : str):
        res = cadastrar_professor(nome, email, senha) 
        if res == None:
            janela.janela.mudar_tela(TelaPrincipalPainel)
        else:
            self.itemconfig(self.text_error, text=res)

    def voltar(self, event):
        janela.janela.mudar_tela(TelaInicialProfessor.TelaInicialProfessor)
