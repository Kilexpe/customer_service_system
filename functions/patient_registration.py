from tkinter import *
master = Tk()

Label(master, text='Nome').grid(row=0)
Label(master, text='Contato ').grid(row=1)
Label(master, text='Descrição').grid(row=2)
entry_nome = Entry(master)
entry_contato = Entry(master)
entry_descricao = Entry(master)

entry_nome.grid(row=0, column=1)
entry_contato.grid(row=1, column=1)
entry_descricao.grid(row=2, column=1)

registrar = Button(master, text="registrar")
voltar = Button(master, text="voltar")
registrar.grid(row=3, column=1)
voltar.grid(row=3, column=0)

master.mainloop()