from tkinter import *
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import Image, ImageTk

# Cores do projeto
co0 = "#2e2d2b"  # Preto
co1 = "#feffff"  # Branco
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Azul escuro
co4 = "#403d3d"  # Cinza escuro
co5 = "#e06636"  # Laranja
co6 = "#038cfc"  # Azul
co7 = "#3fbfb9"  # Verde água
co8 = "#263238"  # Verde escuro
co9 = "#e9edf5"  # Cinza claro

# Criando janela principal
janela = Tk()
janela.title("")
janela.geometry("900x600")
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

# Estilo da interface
style = ttk.Style(janela)
style.theme_use("clam")

# Frames da interface
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief="flat")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Abrindo e configurando a imagem do logo
app_img = Image.open('inventario.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

# Adicionando o logo à interface
app_logo = Label(
    frameCima, 
    image=app_img, 
    text=" Inventário Doméstico", 
    width=900, 
    compound=LEFT, 
    relief=RAISED, 
    anchor=NW, 
    font=('Verdana 20 bold'), 
    bg=co1, 
    fg=co4
)
app_logo.place(x=0, y=0)

# Executando a janela
janela.mainloop()
