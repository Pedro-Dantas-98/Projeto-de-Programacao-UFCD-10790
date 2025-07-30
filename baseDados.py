import sqlite3
from pathlib import Path

class BaseDados:
    def __init__(self, nomeBD: str):
        #Determinar a pasta onde fica guardado o ficheiro da base de dados
        pastaBD = Path("data")
        pastaBD.mkdir(exist_ok=True)
        self.pathBD = pastaBD / f"{nomeBD}.bd"

        #Conectar à base de dados e iniciar o cursor
        self.ligacao = sqlite3.connect(self.pathBD)
        self.cursor = self.ligacao.cursor()
        self.criarTabela()

    def criarTabela(self):
        #Criar uma tabela quando a base de dados é iniciada pela primeira vez
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT
            )
        """)
        self.ligacao.commit()

    def puxarItems(self):
        self.cursor.execute("SELECT id, nome FROM items")
        return self.cursor.fetchall()

    def fecharLigacao(self):
        self.ligacao.close()