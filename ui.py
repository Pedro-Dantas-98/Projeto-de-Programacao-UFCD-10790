import tkinter as tk
from tkinter import ttk

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #Janela
        self.title("Projeto UFCD 10790")
        self.resizable(False, False)
        larguraEcra = self.winfo_screenwidth()
        alturaEcra = self.winfo_screenheight()
        larguraJanela = 800
        alturaJanela = 400
        centerX = (larguraEcra - larguraJanela) // 2
        centerY = (alturaEcra - alturaJanela) // 2
        self.geometry(f'{larguraJanela}x{alturaJanela}+{centerX}+{centerY}')

        #Bases de Dados
        frameBD = tk.Frame(self, padx = 2, pady = 2)
        frameBD.pack(anchor = tk.NW)
        textoBD = tk.Label(frameBD, text = "Selecione uma lista:")
        textoBD.pack(anchor = tk.NW)
        listaBD = tk.Listbox(frameBD, width = 17, height = 3)
        listaBD.insert(0, " Jogos")
        listaBD.insert(1, " Filmes")
        listaBD.insert(2, " Series")
        listaBD.bind('<Double-1>', self.selecionarBD)
        listaBD.pack(anchor=tk.NW, padx = 2, pady = 2)
        
        #Botões
        frameBotoes = tk.Frame(self)
        frameBotoes.pack(side = tk.BOTTOM, anchor = tk.W, pady = 10)

        botaoRegistar = tk.Button(frameBotoes, text = "Registar", width = 14, height = 3)
        botaoRegistar.pack(anchor = tk.SW, padx = 4, pady = 2)
        botaoEditar = tk.Button(frameBotoes, text = "Editar", width = 14, height = 3)
        botaoEditar.pack(anchor = tk.SW, padx = 4, pady = 2)
        botaoVisualizar = tk.Button(frameBotoes, text = "Visualizar", width = 14, height = 3)
        botaoVisualizar.pack(anchor = tk.SW, padx = 4, pady = 2)
        botaoEstatistica = tk.Button(frameBotoes, text = "Estatísticas", width = 14, height = 3)
        botaoEstatistica.pack(anchor = tk.SW, padx = 4, pady = 2)
        botaoBackup = tk.Button(frameBotoes, text = "Backup", width = 14, height = 3)
        botaoBackup.pack(anchor = tk.SW, padx = 4, pady = 2)
        
        #Barra de pesquisa
        framePesquisa = tk.Frame(self, bg="yellow")
        framePesquisa.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=5)

        barraPesquisa = tk.Entry(framePesquisa, width=30)
        barraPesquisa.pack(side=tk.RIGHT)

        textoPesquisa = tk.Label(framePesquisa, text="Pesquisar:")
        textoPesquisa.pack(side=tk.RIGHT, padx=5)

    def selecionarBD(self, event):
        print("Base de dados selecionada")
        
