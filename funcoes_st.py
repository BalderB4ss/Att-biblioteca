import sqlite3
import pandas as pd
import streamlit as st

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
        st.error(f"Deu esse erro na conexão: {erro}")

def cadastrar_livro():
    conexao_base()
    try:
        print("Cadastrando livro!\n")
        titulo = st.text_input("Digite o nome do livro: \n")
        if titulo:
            autor = st.text_input("Digite o autor do livro: \n")
            if autor:
                ano = st.text_input("Digite o ano de lançamento: \n")
                if ano:
                    cadastro = st.button("Cadastrar")
                    if cadastro:
                        cursor.execute("""
                INSERT INTO livros(titulo,autor,ano,disponivel)
                Values (?,?,?,?)""",(titulo,autor,ano,"Sim"))
                        conexao.commit()
                        st.success("Sucesso ao cadastrar o livro!")
    except Exception as erro:
        st.error("Erro ao cadastrar livro | ERRO:{erro}")
    finally:
        if conexao:
            conexao.close()
def listar_livros():
    conexao_base()
    try:
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        tabela_livros = {
            "id": [linha[0] for linha in livros],
            "titulo": [linha[1] for linha in livros],
            "autor": [linha[2] for linha in livros],
            "ano": [linha[3] for linha in livros],
            "disponivel": [":green[Sim]" if linha [4] == "Sim" else ":red[Não]" for linha in livros]}
        st.table(tabela_livros, border = "horizontal")
    except Exception as erro:
        st.error("\nErro ao listar | ERRO:{erro}")
    finally:
        if conexao:
            conexao.close()

def id_livros():
    conexao_base()
    try:
        cursor.execute("SELECT * FROM livros")
        livros = [linha[0] for linha in cursor.fetchall()]
        return livros
    except Exception as erro:
        st.error()



def disponibilidade():
    conexao_base()
    ids = id_livros()
    try:
        if not ids:
            st.warning("Nenhum livro cadastrado!")
            return    
        id = st.selectbox("Selecione o id do livro que deseja alterar a disponibilidade.",ids)
        if st.button("Alterar disponibilidade"):
            cursor.execute("""SELECT disponivel FROM livros WHERE id = ?""",(id,))
            retorno = cursor.fetchone()
            if retorno[0] == "Sim":
                cursor.execute("""
        UPDATE livros
        SET disponivel = ?
        WHERE id = ?
        """,("Não",id))
                conexao.commit()
                st.success("Alteração feita com sucesso!")
            elif retorno[0] == "Não":
                cursor.execute("""
        UPDATE livros
        SET disponivel = ?
        WHERE id = ?
        """,("Sim",id))
                conexao.commit()
                st.success("Alteração feita com sucesso!")
    except Exception as erro:
        st.error(f"\nAlgo deu errado! | ERRO:{erro}")
    finally:
        if conexao:
            conexao.close()
def remover_livro():
    conexao_base()
    ids = id_livros()
    try:
        if not ids:
            st.warning("Nenhum livro cadastrado!")
            return
        id = st.selectbox("Escolha o id do livro que deseja remover!",ids)
        if st.button("Remover livro⚠"):
            cursor.execute("DELETE FROM livros WHERE id =?", (id,))
            conexao.commit()
            if cursor.rowcount > 0:
                st.success("\nLivro removido com sucesso!")
            else:
                print("\nNenhum livro cadastrado com o ID fornecido!")
    except Exception as erro:
        st.error("Erro ao tentar excluir o livro {erro}")
    finally:
        if conexao:
            conexao.close()