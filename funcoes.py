import sqlite3
# Fazendo conexão
def conexao():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL
    ano INTERGER,
    disponivel TEXT)""")
    except Exception as erro:
        print("Deu esse erro na conexão: {erro}")

