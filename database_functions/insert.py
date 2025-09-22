import mysql.connector

def Insert_Database(nome_var, contato_var, descricao_var):
    nome = nome_var.get()
    contato = contato_var.get()
    descricao = descricao_var.get() 

    values = [nome,contato,descricao]
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="customer_service_system_db"
    )

    query = database.cursor()

    query.execute("INSERT INTO ficha (nome, contato, descricao) VALUES (%s, %s, %s)", values)

    database.commit()