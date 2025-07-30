import tkinter as tk
from tkinter import messagebox

class MenuEditarItem(tk.Toplevel):
    def __init__(self, parent, selecaoBD, bd, itemID, atualizarLista):
        super().__init__(parent)
        self.selecaoBD = selecaoBD
        self.bd = bd
        self.atualizarLista = atualizarLista
        self.itemID = itemID
        
        #UI do sub-menu de editar items
        self.title(f"Projeto UFCD 10790 - {self.selecaoBD.capitalize()} - Editar Item")
        self.configurarJanela(700, 350)
        self.transient(parent)
        self.grab_set()
        
        #Campos de entrada de dados
        self.camposDados = []
        self.entradas = {}
        
        #Formatos
        if self.selecaoBD == "jogos":
            self.camposDados = [
                ("Título", "titulo"),
                ("Sinopse", "sinopse"),
                ("Gênero", "genero"),
                ("Plataforma", "plataforma"),
                ("Estreia (AAAA-MM-DD)", "estreia"),
                ("Tempo Jogado (h)", "tempo_jogado"),
                ("Rating", "rating"),
            ]
        elif self.selecaoBD == "filmes":
            self.camposDados = [
                ("Título", "titulo"),
                ("Sinopse", "sinopse"),
                ("Gênero", "genero"),
                ("Realizador", "realizador"),
                ("Estreia (AAAA-MM-DD)", "estreia"),
                ("Duração (HH:MM)", "duracao"),
                ("Rating", "rating"),
            ]
        elif self.selecaoBD == "series":
            self.camposDados = [
                ("Título", "titulo"),
                ("Sinopse", "sinopse"),
                ("Gênero", "genero"),
                ("Estreia (AAAA-MM-DD)", "estreia"),
                ("Temporadas", "temporadas"),
                ("Episódios", "episodios"),
                ("Rating", "rating"),
            ]
        else:
            tk.Label(self, text = "Não foi possível aceder à base de dados.").pack()
            self.destroy
        
        #Puxar os dados do item selecionado
        dados = self.bd.puxarItemSelecionado(self.itemID)
        if not dados:
            tk.Label(self, text = "Não foi possível encontrar o item na base de dados.").pack()
            self.after(2000, self.destroy)
            return

        #Recriar os campos para poder editar
        for i, (label_text, key) in enumerate(self.camposDados, start=1):
            tk.Label(self, text=label_text).pack()
            entry = tk.Entry(self)
            entry.pack()
            entry.insert(0, str(dados[i]) if dados[i] is not None else "")
            self.entradas[key] = entry
            
        #Guardar os dados inseridos
        def guardarDados():
            #Atualizar os dados na base de dados
            try:
                if self.selecaoBD == "jogos":
                    self.bd.cursor.execute("""
                        UPDATE items SET
                        titulo=?, sinopse=?, genero=?, plataforma=?, estreia=?, tempo_jogado=?, rating=?
                        WHERE id=?
                    """, (
                        self.entradas["titulo"].get(),
                        self.entradas["sinopse"].get(),
                        self.entradas["genero"].get(),
                        self.entradas["plataforma"].get(),
                        self.entradas["estreia"].get(),
                        float(self.entradas["tempo_jogado"].get()),
                        float(self.entradas["rating"].get()),
                        self.itemID
                    ))
                elif self.selecaoBD == "filmes":
                    self.bd.cursor.execute("""
                        UPDATE items SET
                        titulo=?, sinopse=?, genero=?, realizador=?, estreia=?, duracao=?, rating=?
                        WHERE id=?
                    """, (
                        self.entradas["titulo"].get(),
                        self.entradas["sinopse"].get(),
                        self.entradas["genero"].get(),
                        self.entradas["realizador"].get(),
                        self.entradas["estreia"].get(),
                        self.entradas["duracao"].get(),
                        float(self.entradas["rating"].get()),
                        self.itemID
                    ))
                elif self.selecaoBD == "series":
                    self.bd.cursor.execute("""
                        UPDATE items SET
                        titulo=?, sinopse=?, genero=?, estreia=?, temporadas=?, episodios=?, rating=?
                        WHERE id=?
                    """, (
                        self.entradas["titulo"].get(),
                        self.entradas["sinopse"].get(),
                        self.entradas["genero"].get(),
                        self.entradas["estreia"].get(),
                        int(self.entradas["temporadas"].get()),
                        int(self.entradas["episodios"].get()),
                        float(self.entradas["rating"].get()),
                        self.itemID
                    ))
                    
                self.bd.ligacao.commit()
                print("O item foi atualizado.")
                messagebox.showinfo("Item Atualizado", f"O item da lista {self.selecaoBD} foi atualizado.")
                
                #Fechar o sub-menu e atualizar a lista de items
                self.destroy()
                self.atualizarLista()
            except Exception as e:
                print(f"Não foi possível guardar os dados. Erro: {e}")
                messagebox.showerror(f"Erro: {e}", f"Não foi possível guardar os dados.")
    
        #UI Botões Sub-Menu Registar
        botaoGuardar = tk.Button(self, text = "Guardar", command = guardarDados)
        botaoGuardar.pack(pady=10)
        botaoCancelar = tk.Button(self, text = "Cancelar", command = self.destroy)
        botaoCancelar.pack()
        
    def configurarJanela(self, larguraJanela: int, alturaJanela: int):
        self.resizable(False, False)
        larguraEcra = self.winfo_screenwidth()
        alturaEcra = self.winfo_screenheight()
        centerX = (larguraEcra - larguraJanela) // 2
        centerY = (alturaEcra - alturaJanela) // 2
        self.geometry(f'{larguraJanela}x{alturaJanela}+{centerX}+{centerY}')