import streamlit as st
import funcoes_st as fnc
import pandas as pd
import sqlite3

st.title("Biblioteca Online")
st.logo("logo.gif")
st.image("imagem1.png", width=400)
aba1,aba2,aba3,aba4 = st.tabs(["Cadastrar Livro","Listar Livros","Remover Livro","Mudar Disponibilidade"])
with aba1:
    st.markdown("Cadastrar um novo livro📚")
    fnc.cadastrar_livro()
with aba2:
    st.markdown("Todos os livros registrados🤓")
    fnc.listar_livros()
with aba3:
    st.markdown("Remover cadastro de livro❗")
    fnc.remover_livro()
with aba4:
    st.markdown("Mudar disponibilidade✅")
    fnc.disponibilidade()