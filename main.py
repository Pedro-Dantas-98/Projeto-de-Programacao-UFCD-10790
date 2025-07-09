from tkinter import *

root = Tk()

root.title("Projeto UFCD 10790")
root.geometry('200x200')

textoBD = Label(root, text = "Selecione uma lista:")
textoBD.grid()
textoBD.pack()

listaBD = Listbox(root)
listaBD.insert(1, "Jogos")
listaBD.insert(2, "Filmes")
listaBD.insert(3, "Series")
listaBD.pack()

root.mainloop()