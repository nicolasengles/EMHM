import tkinter as tk
from PIL import Image, ImageTk
from sgbd import autenticar_usuario
import janela
from TelaMenuPrincipal import TelaMenuPrincipal
import TelaInicial

class TelaLoginAluno(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        # Carrega e desenha o fundo
        img_fundo = Image.open('images/imagemfundo0.png')
        self.imagem_fundo = ImageTk.PhotoImage(img_fundo)
        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)

        # text
        self.create_text(640, 200,
            text="LOGIN",
            font=("Sylfaen", 48, "bold"),
            fill="black",
            anchor='n'
        )

        # 1º Entry: “Digite seu email"
        placeholder_email = "Digite seu e-mail (@p4ed.com):"
        entry_email = tk.Entry(self, font=("Arial", 16), fg="gray")
        entry_email.insert(0, placeholder_email)
        self.create_window(640, 320, window=entry_email, anchor='n', width=500)

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

        # 2º Entry: “Digite sua senha"
        placeholder_senha = "Digite sua senha:"
        entry_senha = tk.Entry(self, font=("Arial", 16), fg="gray", show="*")
        entry_senha.insert(0, placeholder_senha)
        self.create_window(640, 370, window=entry_senha, anchor='n', width=500)

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

        # Botao "ENTRAR"	
        btn_entrar_tag = 'btn_entrar'
        self.create_text(640, 435,
            text="ENTRAR",
            font=("Sylfaen", 24, "bold"),
            fill="green",
            anchor='n',
            tags=(btn_entrar_tag,)
        )
        self.tag_bind(btn_entrar_tag, '<Button-1>', lambda e: self.entrar(entry_email.get(), entry_senha.get()))

        # Botão “SAIR”  
        btn_sair_tag = 'btn_sair'
        self.create_text(640, 480,
            text="SAIR",
            font=("Sylfaen", 24, "bold"),
            fill="red",
            anchor='n',
            tags=(btn_sair_tag,)
        )
        self.tag_bind(btn_sair_tag, '<Button-1>', lambda e: janela.janela.mudar_tela(TelaInicial.TelaInicial))

        self.text_error = self.create_text(640, 407,
                text="",
                font=("Sylfaen", 12, "bold"),
                fill="red",
                anchor='n'
            )
        
        btn_mute_tag = 'btn_mute'
        self.create_text(1150, 650,
            text="DESATIVAR/ATIVAR MÚSICA",
            font=("Sylfaen", 13, "bold"),
            fill="brown",
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

    def entrar(self, email : str, senha : str):
        res = autenticar_usuario(0, email, senha) 
        if res == None:
            janela.janela.mudar_tela(TelaMenuPrincipal)
        else:
            self.itemconfig(self.text_error, text=res)