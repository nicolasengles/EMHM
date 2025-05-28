import tkinter as tk
from PIL import Image, ImageTk
from TelaPartida import *
from emhm import EMHM

class TelaMenuPrincipal(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master)
        
        # --- Load & resize images ---
        bg_img         = tk.PhotoImage(file='images/imagemfundo0.png')
        raw_title      = Image.open(r"images/EXPEDICAO_DO_MILHAO.png").resize((656, 62), Image.LANCZOS)
        title_img      = ImageTk.PhotoImage(raw_title)
        raw_button_img = Image.open(r"images/Frame.png").resize((203, 58), Image.LANCZOS)
        button_img     = ImageTk.PhotoImage(raw_button_img)
        raw_button_2_img = Image.open(r"images/Frame_3.png").resize((203,58), Image.LANCZOS)
        button_2_img   = ImageTk.PhotoImage(raw_button_2_img)

        # --- Create canvas and draw background & title ---
        self.pack(fill="both", expand=True)
        self.create_image(0, 0, image=bg_img,     anchor=tk.NW)
        self.create_image(640, 200, image=title_img, anchor='n')

        # --- First button area ---
        btn_x, btn_y = 640, 200 + 62 + 15
        btn_w, btn_h = 203, 58

        rect1 = self.create_rectangle(
            btn_x - btn_w/2, btn_y,
            btn_x + btn_w/2, btn_y + btn_h,
            fill='', outline=''
        )
        img1 = self.create_image(btn_x, btn_y, image=button_img, anchor='n')

        def on_first_click(event):
            print("Primeiro botão clicado")
            EMHM.mudar_tela(EMHM.janela, TelaPartida)

        for tag in (rect1, img1):
            self.tag_bind(tag, '<Button-1>', on_first_click)

        # --- Second button right below the first ---
        btn2_y = btn_y + btn_h + 30  # 30px gap
        rect2 = self.create_rectangle(
            btn_x - btn_w/2, btn2_y,
            btn_x + btn_w/2, btn2_y + btn_h,
            fill='', outline=''
        )
        img2 = self.create_image(btn_x, btn2_y, image=button_2_img, anchor='n')

        def on_second_click(event):
            print("Segundo botão clicado")

        for tag in (rect2, img2):
            self.tag_bind(tag, '<Button-1>', on_second_click)

        # --- Keep references to prevent GC ---
        master.bg_img     = bg_img
        master.title_img  = title_img
        master.button_img = button_img
