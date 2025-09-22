from tkinter import *
import sys
import os
from tkinter import StringVar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database_functions.insert import *


master = Tk()

nome_var = StringVar()
contato_var = StringVar()
descricao_var = StringVar()

Label(master, text='Nome').grid(row=0)
Label(master, text='Contato ').grid(row=1)
Label(master, text='Descrição').grid(row=2)
entry_nome = Entry(master, textvariable=nome_var)
entry_contato = Entry(master, textvariable=contato_var)
entry_descricao = Entry(master, textvariable=descricao_var)

entry_nome.grid(row=0, column=1)
entry_contato.grid(row=1, column=1)
entry_descricao.grid(row=2, column=1)

registrar = Button(
    master, 
    text="registrar", 
    command = lambda: Insert_Database(nome_var, contato_var, descricao_var)
    )

voltar = Button(master, text="voltar")
registrar.grid(row=3, column=1)
voltar.grid(row=3, column=0)


master.mainloop()