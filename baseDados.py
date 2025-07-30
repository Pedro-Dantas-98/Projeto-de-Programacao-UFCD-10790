import sqlite3
from pathlib import Path

class BaseDados:
    def __init__(self, nomeBD: str):
        #Determinar a pasta onde fica guardado o ficheiro da base de dados
        self.nomeBD = nomeBD
        pastaBD = Path("data")
        pastaBD.mkdir(exist_ok=True)
        self.pathBD = pastaBD / f"{nomeBD}.bd"

        #Conectar à base de dados e iniciar o cursor
        self.ligacao = sqlite3.connect(self.pathBD)
        self.cursor = self.ligacao.cursor()
        self.criarTabela()

    def criarTabela(self):
        #Criar uma tabela quando a base de dados é iniciada pela primeira vez
        if self.nomeBD == "jogos":
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo VARCHAR(255),
                    sinopse VARCHAR(255),
                    genero VARCHAR(15),
                    plataforma VARCHAR(15),
                    estreia DATE,
                    tempo_jogado DECIMAL(3,1),
                    rating DECIMAL(3,1)
                )
            """)
        elif self.nomeBD == "filmes":
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo VARCHAR(255),
                    sinopse VARCHAR(255),
                    genero VARCHAR(15),
                    realizador VARCHAR(50),
                    estreia DATE,
                    duracao TIME,
                    rating DECIMAL(3,1)
                )
            """)
        elif self.nomeBD == "series":
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo VARCHAR(255),
                    sinopse VARCHAR(255),
                    genero VARCHAR(15),
                    estreia DATE,
                    temporadas INTEGER,
                    episodios INTEGER,
                    rating DECIMAL(3,1)
                )
            """)
        else:
            raise ValueError(f"Não foi possível aceder à base de dados.")    
        self.ligacao.commit()

    def puxarItems(self):
        #Função de puxar os items todos da base de dados selecionada
        self.cursor.execute("SELECT id, titulo FROM items")
        return self.cursor.fetchall()
    
    def puxarItemSelecionado(self, id: int):
        #Função de puxar um item especifico baseado no seu ID
        self.cursor.execute("SELECT * FROM items WHERE id = ?", (id,))
        return self.cursor.fetchone()
    
    def pesquisarItemNome(self, termo):
        #Função que seleciona o item que corresponde ao termo de pesquisa
        termo_like = f"%{termo}%"
        self.cursor.execute("""
            SELECT id, titulo FROM items
            WHERE titulo LIKE ?
        """, (termo_like,))
        return self.cursor.fetchall()

    def fecharLigacao(self):
        #Fechar a ligação à base de dados
        self.ligacao.close()