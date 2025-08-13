from tkinter import *
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd

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

# Executando a janela
janela.mainloop()
