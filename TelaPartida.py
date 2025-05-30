import tkinter as tk
from PIL import Image, ImageTk
import sys
from TelaGameOver import TelaGameOver

class TelaPartida(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        # inicializa e empacota
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        # 1) carrega e mantém referências das imagens
        self.imagem_fundo = tk.PhotoImage(file='images/imagemfundo0.png')
        raw_nivel = Image.open('images/NivelDeDificuldade.png').resize((300, 20), Image.LANCZOS)
        self.imagem_nivel = ImageTk.PhotoImage(raw_nivel)
        raw_alt = Image.open('images/Alternativa.png').resize((330, 62), Image.LANCZOS)
        self.imagem_alt = ImageTk.PhotoImage(raw_alt)

        # 2) desenha o fundo e camadas de imagens
        self.create_image(0, 0, image=self.imagem_fundo, anchor='nw', tags=('bg',))
        self.create_image(1000, 36, image=self.imagem_nivel, anchor='n')
        for x, y in [(380,280), (880,280), (880,380), (380,380), (630,480)]:
            self.create_image(x, y, image=self.imagem_alt, anchor='n')

        # 3) desenha textos fixos
        self.create_text(1250, 32,
                         text="FÁCIL",
                         font=("IM FELL ENGLISH SC", 18, "bold"),
                         fill="green",
                         anchor='ne')
        self.create_text(width/2, 190,
                         text="Qual foi o objetivo do Tratado de Versalhes?",
                         font=("Californian FB", 32, "bold"),
                         fill="darkred",
                         anchor='center')
        self.create_text(50, 35,
                         text="QUESTÃO 1",
                         font=("Californian FB", 22, "bold"),
                         fill="darkred",
                         anchor='nw')

        # 4) desenha textos das alternativas
        alternativas = [
            (380,310, "A) Impor sanções econômicas à Alemanha"),
            (380,410, "B) Promover a paz mundial"),
            (880,310, "C) Dividir a Alemanha em várias regiões"),
            (880,410, "D) Estabelecer a Liga das Nações"),
            (630,510, "E) Nenhuma das alternativas"),
        ]
        for x, y, txt in alternativas:
            self.create_text(x, y,
                             text=txt,
                             font=("Californian FB", 13, "bold"))

        # 5) cria o “botão” DESISTIR usando tag para imagem+texto
        btn_tag = 'btn_desistir'
        self.create_image(630, 660,
                          image=self.imagem_alt,
                          anchor='center',
                          tags=(btn_tag,))
        self.create_text(630, 660,
                         text="DESISTIR",
                         font=("Californian FB", 18, "bold"),
                         fill="darkred",
                         anchor='center',
                         tags=(btn_tag,))

        # 6) vincula clique na tag para chamar handler
        self.tag_bind(btn_tag, '<Button-1>', self._on_desistir)

    def _on_desistir(self, event):
        # debug opcional:
        print("Clique em DESISTIR detectado")
        self.desistir()

    def desistir(self):
        # substitui a TelaPartida pela TelaGameOver
        self.destroy()
        TelaGameOver(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    TelaPartida(root)
    root.mainloop()