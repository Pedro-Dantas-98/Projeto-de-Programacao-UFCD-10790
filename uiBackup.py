import tkinter as tk
from tkinter import messagebox, filedialog
import shutil
from datetime import datetime
from pathlib import Path
from baseDados import BaseDados

class MenuBackup(tk.Toplevel):
    def __init__(self, parent, selecaoBD, bd, atualizarLista):
        super().__init__(parent)
        self.bd = bd
        self.selecaoBD = selecaoBD
        self.atualizarLista = atualizarLista
        
        #UI do sub-menu de registar items
        self.title(f"Projeto UFCD 10790 - {self.selecaoBD.capitalize()} - Gerir Backups")
        self.configurarJanela(700, 350)
        self.transient(parent)
        self.grab_set()
        
        #UI Botões Sub-Menu Registar
        botaoCriar = tk.Button(self, text = "Criar Backup", command = self.criarBackup)
        botaoCriar.pack()
        botaoRestaurar = tk.Button(self, text = "Restaurar Dados", command = self.restaurarDados)
        botaoRestaurar.pack()
        botaoCancelar = tk.Button(self, text = "Cancelar", command = self.destroy)
        botaoCancelar.pack()
        
    def configurarJanela(self, larguraJanela: int, alturaJanela: int):
        self.resizable(False, False)
        larguraEcra = self.winfo_screenwidth()
        alturaEcra = self.winfo_screenheight()
        centerX = (larguraEcra - larguraJanela) // 2
        centerY = (alturaEcra - alturaJanela) // 2
        self.geometry(f'{larguraJanela}x{alturaJanela}+{centerX}+{centerY}')
        
    def criarBackup(self):
        if not self.bd:
            messagebox.showwarning("Aviso", "É necessário selecionar uma base de dados.")
            return

        try:
            #Indicar o ficheiro bd original
            pathBDOriginal = self.bd.pathBD

            #Criar uma pasta para guardar os backups
            pastaBackups = Path("data/backups")
            pastaBackups.mkdir(parents=True, exist_ok=True)

            #Guardar o nome e o timestamp do novo ficheiro e o path para a pasta de backups
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nomeBackup = f"{self.selecaoBD}_backup_{timestamp}.bd"
            pathBackup = pastaBackups / nomeBackup

            #Criar o backup
            shutil.copy(pathBDOriginal, pathBackup)

            messagebox.showinfo("Backup Criado", f"O ficheiro de backup foi criado e guardado em: {pathBackup}")
        except Exception as e:
            messagebox.showerror(f"Erro: {e}", f"Não foi possível criar o backup.")
                
    def restaurarDados(self):
        if not self.bd:
            messagebox.showwarning("Aviso", "É necessário selecionar uma base de dados.")
            return

        #Selecionar o ficheiro backup na pasta de backups
        pastaBackups = Path("data/backups")
        if not pastaBackups.exists():
            messagebox.showinfo("Info", "Não existem ficheiros de backup para selecionar.")
            return

        pathBackup = filedialog.askopenfilename(
            title = "Selecione o ficheiro de backup",
            initialdir = str(pastaBackups.resolve()),
            filetypes = [("SQLite Database Files", "*.bd"), ("All files", "*.*")]
        )

        if not pathBackup:
            return

        try:
            #Indicar o ficheiro bd original
            pathBDOriginal = self.bd.pathBD
            
            #Fechar a ligação antes de restaurar os dados
            self.bd.fecharLigacao()

            #Copiar os dados do backup para o ficheiro da base de dados
            shutil.copy(pathBackup, pathBDOriginal)

            #Abrir a ligação
            self.bd = BaseDados(self.selecaoBD)
            
            #Aceder aos items presentes na base de dados
            self.atualizarLista()

            messagebox.showinfo("Restauro Concluido", "Os dados da base de dados foram restaurados.")
        except Exception as e:
            messagebox.showerror(f"Erro: {e}", "Não foi possível restaurar os dados.")