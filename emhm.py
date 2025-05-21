from tkinter import *
from tkinter import ttk

janela = Tk()
janela.geometry('1280x720')
janela.title('Expedição do Milhão: Histórias e Mapas')
arquivo_imagem_fundo = PhotoImage(file='images/imagemfundo0.png')
imagem_fundo = Label(janela, image = arquivo_imagem_fundo)
imagem_fundo.place(x = -2, y = 0)
tela = ttk.Frame(janela, width=1280, height=720)
tela.grid()
ttk.Label(tela, text="Hello World!").place(x=0,y=0)
ttk.Button(tela, text="Quit", command=janela.destroy).grid(column=1, row=0)
janela.mainloop()