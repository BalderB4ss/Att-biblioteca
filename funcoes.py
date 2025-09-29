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
    conexao_base()
    print("Cadastrando livro")
    titulo = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de lançamento: ")
    cursor.execute("""
INSERT INTO livros(titulo,autor,ano,disponivel)
Values (?,?,?,?)""",(titulo,autor,ano,"Sim"))
    conexao.commit()

def listar_livros():
    conexao_base()
    cursor.execute("SELECT * FROM livros")
    for linha in cursor.fetchall():
        print(f"ID: {linha[0]} | Título: {linha[1]} | Autor: {linha[2]} | Ano: {linha[3]} | Disponível: {linha[4]}")

def disponibilidade():
    conexao_base()
    id_livro = int(input("Qual o ID do livro que deseja alterar a disponibilidade? "))
    try:    
        cursor.execute("""SELECT disponivel FROM livros WHERE id = ?""",(id_livro,))
        retorno = cursor.fetchone()
        if retorno[0] is None:
            print("ID não encontrado na tabela!")
        if retorno[0] == "Sim":
            cursor.execute("""
    UPDATE livros
    SET disponivel = ?
    WHERE id = ?
    """,("Não",id_livro))
            conexao.commit()
        if retorno[0] == "Não":
            cursor.execute("""
    UPDATE livros
    SET disponivel = ?
    WHERE disponivel = ?
    """,("Sim",id_livro))
            conexao.commit()
    except Exception as erro:
        print(f"Algo deu errado! ERRO:{erro}")