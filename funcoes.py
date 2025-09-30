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
    try:
        print("Cadastrando livro!\n")
        print("-"*37)
        titulo = input("Digite o nome do livro: \n")
        autor = input("Digite o autor do livro: \n")
        ano = input("Digite o ano de lançamento: \n")
        cursor.execute("""
    INSERT INTO livros(titulo,autor,ano,disponivel)
    Values (?,?,?,?)""",(titulo,autor,ano,"Sim"))
        conexao.commit()
        print("Sucesso ao cadastrar o livro!")
    except Exception as erro:
        print("Erro ao cadastrar livro | ERRO:{erro}")
    finally:
        if conexao:
            conexao.close()
def listar_livros():
    conexao_base()
    try:
        print("-"*37)
        cursor.execute("SELECT * FROM livros")
        for linha in cursor.fetchall():
            print(f"\nID: {linha[0]} | Título: {linha[1]} | Autor: {linha[2]} | Ano: {linha[3]} | Disponível: {linha[4]}")
            print("-"*37)
    except Exception as erro:
        print("\nErro ao listar | ERRO:{erro}")
    finally:
        if conexao:
            conexao.close()

def disponibilidade():
    conexao_base()
    id_livro = int(input("\nQual o ID do livro que deseja alterar a disponibilidade? "))
    try:    
        print("-"*37)
        cursor.execute("""SELECT disponivel FROM livros WHERE id = ?""",(id_livro,))
        retorno = cursor.fetchone()
        if retorno[0] is None:
            print("\nID não encontrado na tabela!")
        if retorno[0] == "Sim":
            cursor.execute("""
    UPDATE livros
    SET disponivel = ?
    WHERE id = ?
    """,("Não",id_livro))
            conexao.commit()
            print("Alteração feita com sucesso!")
        if retorno[0] == "Não":
            cursor.execute("""
    UPDATE livros
    SET disponivel = ?
    WHERE disponivel = ?
    """,("Sim",id_livro))
            conexao.commit()
            print("Alteração feita com sucesso!")
    except Exception as erro:
        print(f"\nAlgo deu errado! | ERRO:{erro}")
    finally:
        if conexao:
            conexao.close()

def remover_livro():
    conexao_base()
    try:
        print("-"*37)
        id_livro = int(input("\nDigite o id do livro que deseja deletar:"))
        cursor.execute("DELETE FROM livros WHERE id =?", (id_livro,))
        conexao.commit()
        if cursor.rowcount > 0:
            print("\nLivro removido com sucesso!")
        else:
            print("\nNenhum livro cadastrado com o ID fornecido!")
    except Exception as erro:
        print("Erro ao tentar excluir o livro {erro}")
    finally:
        if conexao:
            conexao.close()