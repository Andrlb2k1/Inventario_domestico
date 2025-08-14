from tkinter import *
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd

# Importando Pillow
from PIL import Image, ImageTk

# Importando Tkcalendar
from tkcalendar import DateEntry

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

# Frame de cima ---------------------------------------------------------------------------------
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

# Frame do meio ---------------------------------------------------------------------------------
# Campos ----------------------------------------------------------------------------------------
l_nome = Label(frameMeio, text="Nome", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief="solid")
e_nome.place(x=130, y=11)

# Sala/Área
l_local = Label(frameMeio, text="Sala/Área", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify='left', relief="solid")
e_local.place(x=130, y=41)

# Descrição
l_descricao = Label(frameMeio, text="Descrição", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify='left', relief="solid")
e_descricao.place(x=130, y=71)

# Marca/Modelo
l_model = Label(frameMeio, text="Marca/Modelo", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_model.place(x=10, y=100)
e_model = Entry(frameMeio, width=30, justify='left', relief="solid")
e_model.place(x=130, y=101)

# Data da compra
l_cal = Label(frameMeio, text="Data da compra", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(
    frameMeio, 
    width=12, 
    background='darkblue', 
    foreground='white', 
    borderwidth=2, 
    year=2024
)
e_cal.place(x=130, y=131)

# Valor da compra
l_valor = Label(frameMeio, text="Valor da compra", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify='left', relief="solid")
e_valor.place(x=130, y=161)

# Número de série
l_serial = Label(frameMeio, text="Número de série", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serial.place(x=10, y=190)
e_serial = Entry(frameMeio, width=30, justify='left', relief="solid")
e_serial.place(x=130, y=191)

# Executando a janela
janela.mainloop()
