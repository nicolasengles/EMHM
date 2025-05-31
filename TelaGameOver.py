import tkinter as tk
from PIL import Image, ImageTk

class TelaGameOver(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        # 1) Inicializa o Canvas já com tamanho
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        # 2) Carrega e guarda a imagem de fundo
        img = Image.open('images/imagemfundo0.png')
        self.imagem_fundo = ImageTk.PhotoImage(img)
        raw_alt = Image.open('images/Alternativa.png').resize((330, 62), Image.LANCZOS)
        self.imagem_alt = ImageTk.PhotoImage(raw_alt)

        # 3) Desenha no Canvas
        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)
        self.create_text(640, 100,
            text="GAME OVER",
            font=("Californian FB", 48, "bold"),
            fill="darkred",
            anchor='n'
        )
        
        self.create_text(640, 200,
            text="PONTUAÇÃO FINAL: 5000 reais",
            font=("Californian FB", 30, "bold"),
            fill="black",
            anchor='n'
        )

        # botão “REINICIAR” — imagem + texto com a mesma tag
        btn_tag = 'btn_reiniciar'
        self.create_image(640, 300,
            image=self.imagem_alt,
            anchor='n',
            tags=(btn_tag,)
        )
        self.create_text(640, 315,
            text="REINICIAR JOGO",
            font=("Californian FB", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_tag,)            # **importante**!
        )

        # vincula clique na tag, usando lambda para descartar o event
        self.tag_bind(btn_tag, '<Button-1>', lambda e: self.reiniciar())

    def reiniciar(self):
        # destrói a tela atual
        self.destroy()

        # faz o import aqui, dentro do método, para evitar
        # o ciclo de importações no topo do arquivo
        from TelaMenuPrincipal import TelaMenuPrincipal
        TelaMenuPrincipal(self.master)






if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    TelaGameOver(root)
    root.mainloop()
