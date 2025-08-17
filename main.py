from tkinter import *
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd

# Importando Pillow
from PIL import Image, ImageTk

# Importando Tkcalendar
from tkcalendar import DateEntry

from view import atualizar_form, deletar_form, inserir_form, ver_form, ver_item

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

# Funções --------------------------------------------------------------------------------------
global tree

# Função inserir
def inserir():
    global imagem, imagem_string, l_imagem
    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    model = e_model.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serial.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, model, data, valor, serie, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos!')
            return

    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

    # Limpando os campos
    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_model.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serial.delete(0, 'end')

    # Atualizando a tabela
    for widget in frameBaixo.winfo_children():
        widget.destroy()
    mostrar()

# Função atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        # Preenchendo os campos
        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_model.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serial.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_local.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_model.insert(0, treev_lista[4])
        e_cal.insert(0, treev_lista[5])
        e_valor.insert(0, treev_lista[6])
        e_serial.insert(0, treev_lista[7])

        # Função interna para confirmação da atualização
        def update():
            global imagem, imagem_string, l_imagem
            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            model = e_model.get()
            data = e_cal.get()
            valor = e_valor.get()
            serie = e_serial.get()
            imagem = imagem_string or treev_lista[7]

            lista_atualizar = [nome, local, descricao, model, data, valor, serie, imagem, id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos!')
                    return

            atualizar_form(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')

            # Limpando campos
            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_model.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_serial.delete(0, 'end')

            botao_confirmar.destroy()

            # Atualizando a tabela
            for widget in frameBaixo.winfo_children():
                widget.destroy()
            mostrar()

        botao_confirmar = Button(
            frameMeio, command=update, text="CONFIRMAR", width=13, height=1,
            bg=co2, fg=co1, font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE
        )
        botao_confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item na tabela!')

# Função deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso!')

        # Atualizando a tabela
        for widget in frameBaixo.winfo_children():
            widget.destroy()
        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item na tabela!')

# Função para abrir imagem
def ver_imagem():
    global l_imagem, imagem, imagem_string

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']
    valor = [int(treev_lista[0])]

    item = ver_item(valor)
    imagem = item[0][8]

    # Abrindo a imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)

# Função para escolher imagem
def escolher_imagem():
    global l_imagem, imagem, imagem_string

    imagem = fd.askopenfilename()
    imagem_string = imagem

    # Abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    # Adicionando o logo à interface
    l_imagem = Label(
        frameMeio, 
        image=imagem, 
        bg=co1, 
        fg=co4
    )
    l_imagem.place(x=700, y=10)

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

# Botões ----------------------------------------------------------------------------------------
# Botão para carregar imagem do item
l_carregar = Label(frameMeio, text="Imagem do item", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)

botao_carregar = Button(
    frameMeio,
    command=escolher_imagem,
    compound=CENTER, 
    anchor=CENTER, 
    text="CARREGAR", 
    width=29, 
    overrelief=RIDGE,  
    font=('ivy 8'), 
    bg=co1, 
    fg=co0
)
botao_carregar.place(x=130, y=221)

# Botão Adicionar
img_add = Image.open('add.png').resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)

botao_inserir = Button(
    frameMeio,
    command=inserir, 
    image=img_add, 
    compound=LEFT, 
    anchor=NW, 
    text="   ADICIONAR", 
    width=95, 
    overrelief=RIDGE,  
    font=('ivy 8'), 
    bg=co1, 
    fg=co0
)
botao_inserir.place(x=330, y=10)

# Botão Atualizar
img_update = Image.open('update.png').resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)

botao_atualizar = Button(
    frameMeio,
    command=atualizar,
    image=img_update, 
    compound=LEFT, 
    anchor=NW, 
    text="   ATUALIZAR", 
    width=95, 
    overrelief=RIDGE,  
    font=('ivy 8'), 
    bg=co1, 
    fg=co0
)
botao_atualizar.place(x=330, y=50)

# Botão Deletar
img_delete = Image.open('delete.png').resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)

botao_deletar = Button(
    frameMeio,
    command=deletar,
    image=img_delete, 
    compound=LEFT,
    anchor=NW, 
    text="   DELETAR", 
    width=95, 
    overrelief=RIDGE,  
    font=('ivy 8'), 
    bg=co1, 
    fg=co0
)
botao_deletar.place(x=330, y=90)

# Botão Ver item
img_item = Image.open('item.png').resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)

botao_ver = Button(
    frameMeio,
    command=ver_imagem,
    image=img_item, 
    compound=LEFT, 
    anchor=NW, 
    text="   VER ITEM", 
    width=95, 
    overrelief=RIDGE,  
    font=('ivy 8'), 
    bg=co1, 
    fg=co0
)
botao_ver.place(x=330, y=221)

# Labels para Total e Quantidade
l_total = Label(
    frameMeio, 
    width=14, 
    height=2, 
    anchor=CENTER, 
    font=('Ivy 17 bold'), 
    bg=co7, 
    fg=co1, 
    relief=FLAT
)
l_total.place(x=450, y=17)

l_valor_total = Label(
    frameMeio, 
    text='  Valor total de todos os itens   ', 
    anchor=NW, 
    font=('Ivy 10 bold'), 
    bg=co7, 
    fg=co1
)
l_valor_total.place(x=450, y=12)

l_qtd = Label(
    frameMeio, 
    width=10, 
    height=2,
    pady=5, 
    anchor=CENTER, 
    font=('Ivy 25 bold'), 
    bg=co7, 
    fg=co1, 
    relief=FLAT
)
l_qtd.place(x=450, y=90)

l_qtd_itens = Label(
    frameMeio, 
    text='Quantidade total de itens', 
    anchor=NW, 
    font=('Ivy 10 bold'), 
    bg=co7, 
    fg=co1
)
l_qtd_itens.place(x=460, y=92)

# Frame de baixo ---------------------------------------------------------------------------------
# Função para mostrar os dados na tabela
def mostrar():
    # Definindo os cabeçalhos
    tabela_head = ['#Item', 'Nome', 'Sala/Área', 'Descrição', 'Marca/Modelo', 'Data da compra', 'Valor da compra', 'Número de série']

    # Lista de itens
    lista_itens = ver_form()

    global tree

    # Configurando Treeview
    tree = ttk.Treeview(
        frameBaixo, 
        selectmode="extended",
        columns=tabela_head, 
        show="headings"
    )

    # Scrollbars
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Posicionando Treeview e Scrollbars
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frameBaixo.grid_rowconfigure(0, weight=12)

    # Configuração das colunas
    hd = ["center"] * len(tabela_head)
    h = [40, 150, 100, 160, 130, 100, 100, 100]

    for n, col in enumerate(tabela_head):
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

    # Inserindo itens na tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)

    # Calculando totais
    quantidade = [iten[6] for iten in lista_itens]
    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    # Atualizando Labels
    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens

# Chamando a função para mostrar os dados
mostrar()

# Executando a janela
janela.mainloop()
