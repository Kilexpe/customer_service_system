from tkinter import *
master = Tk()
master.geometry("500x500")

menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Cadastro de paciente')
filemenu.add_command(label='Agendar Consulta')
filemenu.add_command(label='Editar/Cancelar Consulta')
filemenu.add_command(label='Registrar Atendimento')
filemenu.add_command(label="Listar Consultas")
filemenu.add_command(label="Relatórios")
filemenu.add_command(label="Sair", command=master.quit)

master.mainloop()