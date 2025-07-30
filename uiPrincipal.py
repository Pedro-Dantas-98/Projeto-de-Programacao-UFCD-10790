import tkinter as tk
from tkinter import messagebox
from baseDados import BaseDados
from uiRegistarItem import MenuRegistarItem
from uiEditarItem import MenuEditarItem

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.selecaoBD = None
        self.bd = None
        
        #Janela
        self.title("Projeto UFCD 10790")
        configurarJanela(self, 800, 400)
        
        #Função de UI do menu principal
        self.uiMenuPrincipal()
        
    def uiMenuPrincipal(self):
        #Configurar a grid
        self.grid_columnconfigure(1, weight = 1, minsize = 300)
        self.grid_columnconfigure(2, weight = 1, minsize = 300)
        self.grid_rowconfigure(1, weight = 1, minsize = 150)  

        #UI Bases de Dados
        frameBD = tk.Frame(self)
        frameBD.grid(row = 0, column = 0, sticky = "nw", padx = 2, pady = (4, 0))
        
        textoBD = tk.Label(frameBD, text = "Selecione uma lista:")
        textoBD.pack(anchor = tk.NW)
        
        self.listaBD = tk.Listbox(frameBD, width = 17, height = 3)
        self.listaBD.insert(0, " Jogos")
        self.listaBD.insert(1, " Filmes")
        self.listaBD.insert(2, " Series")
        self.listaBD.bind('<<ListboxSelect>>', self.selecionarBD)
        self.listaBD.pack(anchor = tk.NW, padx = 2, pady = 2)
        
        #UI Botões
        frameBotoes = tk.Frame(self)
        frameBotoes.grid(row = 1, column = 0, sticky = "n", padx = 1, pady = (10, 0))

        botaoRegistar = tk.Button(frameBotoes, text = "Registar", command = self.registarItem, width = 14, height = 3)
        botaoRegistar.pack(anchor = tk.W, padx = 4, pady = 2)
        botaoEditar = tk.Button(frameBotoes, text = "Editar", command = self.editarItem, width = 14, height = 3)
        botaoEditar.pack(anchor = tk.W, padx = 4, pady = 2)
        botaoEliminar = tk.Button(frameBotoes, text = "Eliminar", width = 14, height = 3)
        botaoEliminar.pack(anchor = tk.W, padx = 4, pady = 2)
        botaoEstatistica = tk.Button(frameBotoes, text = "Estatísticas", width = 14, height = 3)
        botaoEstatistica.pack(anchor = tk.W, padx = 4, pady = 2)
        botaoBackup = tk.Button(frameBotoes, text = "Backup", width = 14, height = 3)
        botaoBackup.pack(anchor = tk.W, padx = 4, pady = 2)
        
        #UI Barra de pesquisa
        framePesquisa = tk.Frame(self)
        framePesquisa.grid(row = 0, column = 2, sticky = "ne", padx = (5, 10), pady = (5, 0))
        
        textoPesquisa = tk.Label(framePesquisa, text = "Pesquisar:")
        textoPesquisa.pack(side = tk.LEFT)

        barraPesquisa = tk.Entry(framePesquisa, width = 30)
        barraPesquisa.pack(side = tk.LEFT)
        
        #UI Lista de items
        frameItems = tk.Frame(self)
        frameItems.grid(row = 0, column = 1, rowspan= 2, columnspan = 2, sticky = "nsew", padx = 5, pady = (35, 10))
        
        scrollbarItems = tk.Scrollbar(frameItems)
        scrollbarItems.pack(side = tk.RIGHT, fill = tk.Y)

        self.listaItems = tk.Listbox(frameItems, width = 80, height = 15, yscrollcommand = scrollbarItems.set)
        self.listaItems.pack(fill = tk.BOTH, expand = True)
        scrollbarItems.config(command = self.listaItems.yview)
        
        #Selecionar BD inicial
        self.listaBD.select_set(0)
        self.selecionarBD(None)    

    def selecionarBD(self, event):
        #Escolher a base de dados selecionada na lista
        selecionadoBD = self.listaBD.curselection()
        
        if not selecionadoBD:
            return
        
        basesDados = ['jogos', 'filmes', 'series']
        self.selecaoBD = basesDados[selecionadoBD[0]]
        self.title(f"Projeto UFCD 10790 - {self.selecaoBD.capitalize()}")
        
        if self.bd:
            self.bd.fecharLigacao()

        self.bd = BaseDados(self.selecaoBD)
        
        #Correr a função de aceder aos items presentes na base de dados selecionada
        self.acederItemsBD()
    
    def acederItemsBD(self):
        #Verificação para evitar erro
        if self.bd is None:
            return 
        
        #Apagar os items presentes na listbox e puxar os items presentes na base de dados
        self.listaItems.delete(0, tk.END)
        itemsBD = self.bd.puxarItems()
        
        #Verificar se a base de dados tem items
        if not itemsBD:
            self.listaItems.insert(tk.END, f"(Não existem items na base de dados {self.selecaoBD})")
        else:
            for itemID, nomeItem in itemsBD:
                self.listaItems.insert(tk.END, f"{itemID}: {nomeItem}")
        
    def registarItem(self):
        MenuRegistarItem(self, self.selecaoBD, self.bd, self.acederItemsBD)

    def editarItem(self):
        selecionadoItem = self.listaItems.curselection()
        if not selecionadoItem:
            print("Não selecionou um item.")
            messagebox.showwarning("Aviso", "É necessário selecionar um item para editar.")
            return
        
        itemTexto = self.listaItems.get(selecionadoItem[0])
        itemID = int(itemTexto.split(":")[0])
        
        MenuEditarItem(self, self.selecaoBD, self.bd, itemID, self.acederItemsBD)

    def eliminarItem(self):
        print("Abrir sub-menu para ver detalhes do item.")

    def verEstatisticas(self):
        print("Abrir sub-janela com estatísticas.")

    def criarBackup(self):
        print("Criar cópia de segurança da base de dados atual.")

def configurarJanela(self, larguraJanela: int, alturaJanela: int):
    self.resizable(False, False)
    larguraEcra = self.winfo_screenwidth()
    alturaEcra = self.winfo_screenheight()
    centerX = (larguraEcra - larguraJanela) // 2
    centerY = (alturaEcra - alturaJanela) // 2
    self.geometry(f'{larguraJanela}x{alturaJanela}+{centerX}+{centerY}')