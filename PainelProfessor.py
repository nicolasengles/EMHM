import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime

class PainelProfessor(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        # Carrega e desenha o fundo

        raw_fundo = Image.open(r'images\black-solid-background-2920-x-1642-jk98dr7udfcq3hqj.jpg')\
            .resize((width, height), Image.LANCZOS)
        
        self.imagem_fundo = ImageTk.PhotoImage(raw_fundo)
        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)

        # 1º Entry: “Digite seu nome”
        placeholder_nome = "Digite seu e-mail:"
        entry_nome = tk.Entry(self, font=("Arial", 16), fg="gray")
        entry_nome.insert(0, placeholder_nome)
        self.create_window(640, 370, window=entry_nome, anchor='n')

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

        # 2º Entry: “Digite seu e-mail”
        placeholder_email = "Digite sua senha:"
        entry_email = tk.Entry(self, font=("Arial", 16), fg="gray")
        entry_email.insert(0, placeholder_email)
        self.create_window(640, 420, window=entry_email, anchor='n')

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

        # text

        self.create_text(640, 300,
            text="PAINEL DO PROFESSOR",
            font=("Arial", 24, "bold"),
            fill="white",
            anchor='n'
        )

        # Botão “SAIR”  
        btn_sair_tag = 'btn_sair'
        self.create_text(640, 520,
            text="SAIR",
            font=("Arial", 18, "bold"),
            fill="red",
            anchor='n',
            tags=(btn_sair_tag,)
        )   

        # Botao "ENTRAR"	
        btn_entrar_tag = 'btn_entrar'
        self.create_text(640, 485,
            text="ENTRAR",
            font=("Arial", 18, "bold"),
            fill="light green",
            anchor='n',
            tags=(btn_entrar_tag,)
        )

        # Horario 

        self.create_text(640, 250,
            text="00:00",
            font=("Arial", 16),
            fill="white",
            anchor='n'
        )


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    PainelProfessor(root)
    root.mainloop()
