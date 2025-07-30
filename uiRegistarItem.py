import tkinter as tk
from tkinter import messagebox

class MenuRegistarItem(tk.Toplevel):
    def __init__(self, parent, selecaoBD, bd, atualizarLista):
        super().__init__(parent)
        self.selecaoBD = selecaoBD
        self.bd = bd
        self.atualizarLista = atualizarLista
        
        #UI do sub-menu de registar items
        self.title(f"Projeto UFCD 10790 - {self.selecaoBD.capitalize()} - Registar Item")
        self.configurarJanela(700, 350)
        self.transient(parent)
        self.grab_set()
        
        #Campos de entrada de dados
        camposDados = []
        entradas = {}

        #Formatos
        camposDados.append(("Título", tk.Entry(self)))
        camposDados.append(("Sinopse", tk.Entry(self)))
        camposDados.append(("Gênero", tk.Entry(self)))
        
        if self.selecaoBD == "jogos":
            camposDados.append(("Plataforma", tk.Entry(self)))
            camposDados.append(("Estreia (AAAA-MM-DD)", tk.Entry(self)))
            camposDados.append(("Tempo Jogado (h)", tk.Entry(self)))
            camposDados.append(("Rating", tk.Entry(self)))
        elif self.selecaoBD == "filmes":
            camposDados.append(("Realizador", tk.Entry(self)))
            camposDados.append(("Estreia (AAAA-MM-DD)", tk.Entry(self)))
            camposDados.append(("Duração (HH:MM)", tk.Entry(self)))
            camposDados.append(("Rating", tk.Entry(self)))
        elif self.selecaoBD == "series":
            camposDados.append(("Estreia (AAAA-MM-DD)", tk.Entry(self)))
            camposDados.append(("Temporadas", tk.Entry(self)))
            camposDados.append(("Episódios", tk.Entry(self)))
            camposDados.append(("Rating", tk.Entry(self)))
            
        #UI Campos
        for textoCampo, entradaDados in camposDados:
            tk.Label(self, text = textoCampo).pack()
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
                messagebox.showinfo("Item Registado", f"O item foi registado na lista {self.selecaoBD}.")
                
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