import tkinter as tk
from PIL import Image, ImageTk

class DbManagement(tk.Canvas):
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
            text="GERENCIAMENTO DE BANCO DE DADOS",
            font=("Arial", 24, "bold"),
            fill="white",
            anchor='n'
        )






if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    DbManagement(root)
    root.mainloop()
    