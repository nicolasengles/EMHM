import tkinter as tk
from PIL import Image, ImageTk
# import janela
# import app
from app import app
# from partida import Partida
import functools
from TelaPartida import TelaPartida

class TelaIniciarPartida(tk.Canvas):
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
        raw_btn = Image.open('images/Alternativa.png')\
                         .resize((330, 62), Image.LANCZOS)
        self.imagem_btn = ImageTk.PhotoImage(raw_btn)

        # 3) desenha fundo e logo
        self.create_image(0, 0, image=self.imagem_fundo, anchor='nw')
        self.create_image(640, 100, image=self.imagem_titulo, anchor='n')
        self.create_image(810, 200, image=self.imagem_subtitulo, anchor='n')

        # 4) “Botão História
        btn_hist_tag = 'btn_historia'
        self.create_image(640, 300,
            image=self.imagem_btn,
            anchor='n',
            tags=(btn_hist_tag)
        )

        self.create_text(640, 315,
            text="HISTÓRIA",
            font=("Californian FB", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_hist_tag)
        )
        
        self.tag_bind(btn_hist_tag, '<Button-1>', functools.partial(self.jogar, materia=0))

        # 5) “Botão Geografia
        btn_geo_tag = 'btn_geografia'
        self.create_image(640, 400,
            image=self.imagem_btn,
            anchor='n',
            tags=(btn_geo_tag)
        )

        self.create_text(640, 415,
            text="GEOGRAFIA",
            font=("Californian FB", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_geo_tag)
        )
        
        self.tag_bind(btn_geo_tag, '<Button-1>', functools.partial(self.jogar, materia=1))

        # 6) “Botão Ambas
        btn_amb_tag = 'btn_ambas'
        self.create_image(640, 500,
            image=self.imagem_btn,
            anchor='n',
            tags=(btn_amb_tag)
        )

        self.create_text(640, 515,
            text="HISTÓRIA E GEOGRAFIA",
            font=("Californian FB", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_amb_tag)
        )
        
        self.tag_bind(btn_amb_tag, '<Button-1>', functools.partial(self.jogar, materia=2))

    def jogar(self, event=None, materia=None):
        # destrói a TelaMenuPrincipal atual
        # self.destroy()
        app.iniciar_partida(materia=materia)
        # abre a TelaPartida
        # janela.janela.mudar_tela(TelaPartida(self.master))


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("1280x720")
#     TelaIniciarPartida(root)
#     root.mainloop()
