from tkinter import *
master = Tk()
master.geometry("500x500")
master

menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Cadastro de paciente')
filemenu.add_command(label='Agendar Consulta')
filemenu.add_command(label='Editar/Cancelar Consulta')
filemenu.add_command(label="Listar Consultas")
filemenu.add_command(label="Relatórios")
filemenu.add_command(label="Sair", command=master.quit)

Button(text="Cadastro de Paciente", width=25).grid(row=1, column=1)
Button(text="Agendar Consulta", width=25).grid(row=2, column=1)
Button(text="Editar/Cancelar Consultar", width=25).grid(row=3, column=1)
Button(text="Listar Consultas", width=25).grid(row=5, column=1)
Button(text="Relatórios", width=25).grid(row=6, column=1)

master.mainloop()