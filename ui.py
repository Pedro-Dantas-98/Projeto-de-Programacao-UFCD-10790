import tkinter as tk

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
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(1, weight = 1)  

        #Bases de Dados
        frameBD = tk.Frame(self)
        frameBD.grid(row = 0, column = 0, sticky = "nw", padx = 2, pady = (4, 0))
        
        textoBD = tk.Label(frameBD, text = "Selecione uma lista:")
        textoBD.pack(anchor = tk.NW)
        
        listaBD = tk.Listbox(frameBD, width = 17, height = 3)
        listaBD.insert(0, " Jogos")
        listaBD.insert(1, " Filmes")
        listaBD.insert(2, " Series")
        listaBD.bind('<Double-1>', self.selecionarBD)
        listaBD.pack(anchor = tk.NW, padx = 2, pady = 2)
        
        #Botões
        frameBotoes = tk.Frame(self)
        frameBotoes.grid(row = 2, column = 0, sticky = "sw", pady = (0, 5))

        botaoRegistar = tk.Button(frameBotoes, text = "Registar", width = 14, height = 3)
        botaoRegistar.pack(anchor = tk.W, padx = 4, pady = 2)
        botaoEditar = tk.Button(frameBotoes, text = "Editar", width = 14, height = 3)
        botaoEditar.pack(anchor = tk.W, padx = 4, pady = 2)
        botaoVisualizar = tk.Button(frameBotoes, text = "Visualizar", width = 14, height = 3)
        botaoVisualizar.pack(anchor = tk.W, padx = 4, pady = 2)
        botaoEstatistica = tk.Button(frameBotoes, text = "Estatísticas", width = 14, height = 3)
        botaoEstatistica.pack(anchor = tk.W, padx = 4, pady = 2)
        botaoBackup = tk.Button(frameBotoes, text = "Backup", width = 14, height = 3)
        botaoBackup.pack(anchor = tk.W, padx = 4, pady = 2)
        
        #Barra de pesquisa
        framePesquisa = tk.Frame(self)
        framePesquisa.grid(row = 0, column = 2, sticky = "ne", padx = 10, pady = (5, 0))
        
        textoPesquisa = tk.Label(framePesquisa, text = "Pesquisar:")
        textoPesquisa.pack(side = tk.LEFT)

        barraPesquisa = tk.Entry(framePesquisa, width = 30)
        barraPesquisa.pack(side = tk.LEFT)

    def selecionarBD(self, event):
        print("Base de dados selecionada")
        
