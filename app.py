import streamlit as st
import funcoes_st as fnc
import pandas as pd
import sqlite3

st.title("Biblioteca Online")

aba1,aba2,aba3,aba4 = st.tabs(["Cadastrar Livro","Listar Livros","Remover Livro","Mudar Disponibilidade"])
with aba1:
    fnc.cadastrar_livro()
with aba2:
    fnc.listar_livros()
with aba3:
    fnc.remover_livro()
with aba4:
    fnc.disponibilidade()