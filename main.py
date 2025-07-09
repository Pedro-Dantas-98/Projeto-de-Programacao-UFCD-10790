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
root.resizable(False, False)

larguraEcra = root.winfo_screenwidth()
alturaEcra = root.winfo_screenheight()
larguraJanela = 130
alturaJanela = 94
centerX = (larguraEcra - larguraJanela) // 2
centerY = (alturaEcra - alturaJanela) // 2
root.geometry(f'{larguraJanela}x{alturaJanela}+{centerX}+{centerY}')

frameBD = Frame(root, padx = 2, pady = 2)
frameBD.pack()

textoBD = Label(root, text = "Selecione uma lista:")
textoBD.pack(anchor=NW)

listaBD = Listbox(root, width = 20, height = 4)
listaBD.insert(0, "Jogos")
listaBD.insert(1, "Filmes")
listaBD.insert(2, "Series")
listaBD.bind('<Double-1>', selecionarBD)
listaBD.pack()

root.mainloop()