from tkinter import *
import mysql.connector

#MYSQL                    
def selecionarBD(event):
    selecaoCursor = listaBD.curselection()
    
    if not selecaoCursor:
        return
    
    indice = selecaoCursor[0]
    nomeBD = ['jogos', 'filmes', 'series']
    selecaoBD = nomeBD[indice].lower()
        
    try:
        ligacao = mysql.connector.connect(
            host = 'localhost',
            user = 'Pedro',
            password = 'Python2025'
        )
        cursor = ligacao.cursor()
        
        cursor.execute("SHOW DATABASES")
        resultados = cursor.fetchall()
        basesDados = [name for (name,) in resultados]
        
        if selecaoBD not in basesDados:
            cursor.execute(f"CREATE DATABASE {selecaoBD}")
            print(f"A base de dados '{selecaoBD}' foi criada.")
        else:
            print(f"A base de dados '{selecaoBD}' já existe.")    
            
        ligacaoSelecao = mysql.connector.connect(
            host = 'localhost',
            user = 'Pedro',
            password = 'Python2025',
            database = selecaoBD
        )
        cursorSelecao = ligacaoSelecao.cursor()
        print(f"Estabelecida ligação à base de dados '{selecaoBD}'.")
    except mysql.connector.Error as erro:
        print(f"Não foi possível estabelecer uma ligação. Erro: '{erro}'")

#Interface                   
root = Tk()

root.title("Projeto UFCD 10790")
root.geometry('200x200')

textoBD = Label(root, text = "Selecione uma lista:")
textoBD.pack()

listaBD = Listbox(root)
listaBD.insert(0, "Jogos")
listaBD.insert(1, "Filmes")
listaBD.insert(2, "Series")
listaBD.bind('<Double-1>', selecionarBD)
listaBD.pack()

root.mainloop()