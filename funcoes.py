import sqlite3
# Fazendo conexão
def conexao_base():
    global cursor
    global conexao
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTERGER,
    disponivel TEXT)""")
    except Exception as erro:
        print(f"Deu esse erro na conexão: {erro}")

def cadastrar_livro():
    print("Cadastrando livro")
    titulo = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de lançamento: ")
    cursor.execute("""
INSERT INTO livros(titulo,autor,ano,disponivel)
Values (?,?,?,?)""",(titulo,autor,ano,"Sim"))
    conexao.commit()