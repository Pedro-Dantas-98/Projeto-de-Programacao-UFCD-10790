import tkinter as tk
from baseDados import BaseDados

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
        botaoEditar = tk.Button(frameBotoes, text = "Editar", width = 14, height = 3)
        botaoEditar.pack(anchor = tk.W, padx = 4, pady = 2)
        botaoVisualizar = tk.Button(frameBotoes, text = "Visualizar", width = 14, height = 3)
        botaoVisualizar.pack(anchor = tk.W, padx = 4, pady = 2)
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
        selecionado = self.listaBD.curselection()
        
        if not selecionado:
            return
        
        basesDados = ['jogos', 'filmes', 'series']
        self.selecaoBD = basesDados[selecionado[0]]
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
        #UI do sub-menu de registar items
        menuRegistar = tk.Toplevel(self)
        menuRegistar.title(f"Projeto UFCD 10790 - {self.selecaoBD} - Registar Item")
        configurarJanela(menuRegistar, 700, 350)
        menuRegistar.transient(self)
        menuRegistar.grab_set()
        
        #Campos de entrada de dados
        camposDados = []

        camposDados.append(("Título", tk.Entry(menuRegistar)))
        camposDados.append(("Sinopse", tk.Entry(menuRegistar)))
        camposDados.append(("Gênero", tk.Entry(menuRegistar)))
        
        if self.selecaoBD == "jogos":
            camposDados.append(("Plataforma", tk.Entry(menuRegistar)))
            camposDados.append(("Estreia (AAAA-MM-DD)", tk.Entry(menuRegistar)))
            camposDados.append(("Tempo Jogado (h)", tk.Entry(menuRegistar)))
            camposDados.append(("Rating", tk.Entry(menuRegistar)))
        elif self.selecaoBD == "filmes":
            camposDados.append(("Realizador", tk.Entry(menuRegistar)))
            camposDados.append(("Estreia (AAAA-MM-DD)", tk.Entry(menuRegistar)))
            camposDados.append(("Duração (HH:MM)", tk.Entry(menuRegistar)))
            camposDados.append(("Rating", tk.Entry(menuRegistar)))
        elif self.selecaoBD == "series":
            camposDados.append(("Estreia (AAAA-MM-DD)", tk.Entry(menuRegistar)))
            camposDados.append(("Temporadas", tk.Entry(menuRegistar)))
            camposDados.append(("Episódios", tk.Entry(menuRegistar)))
            camposDados.append(("Rating", tk.Entry(menuRegistar)))
            
        entradas = {}
        
        for textoCampo, entradaDados in camposDados:
            tk.Label(menuRegistar, text = textoCampo).pack()
            entradaDados.pack()
            entradas[textoCampo] = entradaDados
            
        #Guardar os dados inseridos
        def guardarDados():
            #Obter os dados de todos os campos para inserir na base de dados
            dados = {}
            for nomeCampo, camposDados in entradas.items():
                dados[nomeCampo] = camposDados.get()
                
            try:
                if self.selecaoBD == "jogos":
                    self.bd.cursor.execute("""
                        INSERT INTO items (titulo, sinopse, genero, plataforma, estreia, tempo_jogado, rating)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (
                        dados["Título"],
                        dados["Sinopse"],
                        dados["Gênero"],
                        dados["Plataforma"],
                        dados["Estreia (AAAA-MM-DD)"],
                        float(dados["Tempo Jogado (h)"]),
                        float(dados["Rating"]),
                    ))
                elif self.selecaoBD == "filmes":
                    self.bd.cursor.execute("""
                        INSERT INTO items (titulo, sinopse, genero, realizador, estreia, duracao, rating)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (
                        dados["Título"],
                        dados["Sinopse"],
                        dados["Gênero"],
                        dados["Realizador"],
                        dados["Estreia (AAAA-MM-DD)"],
                        dados["Duração (HH:MM)"],
                        float(dados["Rating"]),
                    ))
                elif self.selecaoBD == "series":
                    self.bd.cursor.execute("""
                        INSERT INTO items (titulo, sinopse, genero, estreia, temporadas, episodios, rating)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (
                        dados["Título"],
                        dados["Sinopse"],
                        dados["Gênero"],
                        dados["Estreia (AAAA-MM-DD)"],
                        int(dados["Temporadas"]),
                        int(dados["Episódios"]),
                        float(dados["Rating"]),
                    ))
                
                self.bd.ligacao.commit()
                print("O item foi registado.")
                
                #Fechar o sub-menu e atualizar a lista de items
                menuRegistar.destroy()
                self.acederItemsBD()
            except Exception as e:
                print(f"Não foi possível guardar os dados. Erro: {e}")

        #UI Botões Sub-Menu Registar
        botaoGuardar = tk.Button(menuRegistar, text = "Guardar", command = guardarDados)
        botaoGuardar.pack(pady=10)
        botaoCancelar = tk.Button(menuRegistar, text = "Cancelar", command = menuRegistar.destroy)
        botaoCancelar.pack()

    def editarItem(self):
        print("Abrir sub-menu para editar item selecionado.")

    def visualizarItem(self):
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