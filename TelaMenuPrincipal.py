import tkinter as tk
from PIL import Image, ImageTk
from TelaIniciarPartida import TelaIniciarPartida
import janela

class TelaMenuPrincipal(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        # 1) inicializa o Canvas já com tamanho
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        # 2) carrega e mantém as imagens
        self.imagem_fundo = tk.PhotoImage(file='images/imagemfundo0.png')
        raw_titulo = Image.open("images/EXPEDICAO_DO_MILHAO.png")\
                          .resize((750, 75), Image.LANCZOS)
        self.imagem_titulo = ImageTk.PhotoImage(raw_titulo)
        raw_sub = Image.open("images/HistoriaseMapas.png")\
                       .resize((500, 65), Image.LANCZOS)
        self.imagem_subtitulo = ImageTk.PhotoImage(raw_sub)
        raw_jogar = Image.open('images/Alternativa.png')\
                         .resize((330, 62), Image.LANCZOS)
        self.imagem_jogar = ImageTk.PhotoImage(raw_jogar)

        # 3) desenha fundo e logo
        self.create_image(0, 0, image=self.imagem_fundo, anchor='nw')
        self.create_image(640, 100, image=self.imagem_titulo, anchor='n')
        self.create_image(810, 200, image=self.imagem_subtitulo, anchor='n')

        # 4) “botão” JOGAR usando Canvas + tag única
        btn_tag = 'btn_jogar'
        self.create_image(640, 300,
            image=self.imagem_jogar,
            anchor='n',
            tags=(btn_tag,)
        )

        self.create_text(640, 315,
            text="JOGAR",
            font=("Californian FB", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_tag,)
        )
        
        self.tag_bind(btn_tag, '<Button-1>', self.jogar)

    def jogar(self, event=None):
        janela.janela.mudar_tela(TelaIniciarPartida(self.master))

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("1280x720")
#     TelaMenuPrincipal(root)
#     root.mainloop()
