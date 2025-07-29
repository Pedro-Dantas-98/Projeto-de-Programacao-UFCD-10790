import tkinter as tk

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Projeto UFCD 10790")
        self.resizable(False, False)

        larguraEcra = self.winfo_screenwidth()
        alturaEcra = self.winfo_screenheight()
        larguraJanela = 130
        alturaJanela = 94
        centerX = (larguraEcra - larguraJanela) // 2
        centerY = (alturaEcra - alturaJanela) // 2
        self.geometry(f'{larguraJanela}x{alturaJanela}+{centerX}+{centerY}')

        frameBD = tk.Frame(self, padx = 2, pady = 2)
        frameBD.pack()

        textoBD = tk.Label(self, text = "Selecione uma lista:")
        textoBD.pack(anchor = tk.NW)

        listaBD = tk.Listbox(self, width = 20, height = 4)
        listaBD.insert(0, "Jogos")
        listaBD.insert(1, "Filmes")
        listaBD.insert(2, "Series")
        listaBD.bind('<Double-1>', self.selecionarBD)
        listaBD.pack()

    def selecionarBD(self, event):
        print("Base de dados selecionada")
        
