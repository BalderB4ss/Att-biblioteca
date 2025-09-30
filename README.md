# 📚 Biblioteca Online

Um simples sistema de gerenciamento de biblioteca feito com **Python** e **SQLite**. Este projeto permite cadastrar, listar, atualizar a disponibilidade e remover livros de um banco de dados local.

## 🧠 Tecnologias Utilizadas

- **Python 3**
- **SQLite3** (banco de dados local)
- **Streamlit** *(opcional, ainda não implementado na interface atual)*

---

## 🚀 Funcionalidades

1. **Listar livros**
2. **Cadastrar um novo livro**
3. **Remover livro existente**
4. **Atualizar disponibilidade de um livro**
5. **Sair do programa**

---

## 🗃️ Estrutura do Banco de Dados

O banco de dados é criado automaticamente com o nome `biblioteca.db` e contém uma única tabela chamada `livros` com os seguintes campos:

| Campo       | Tipo     | Descrição                                       |
|-------------|----------|-------------------------------------------------|
| `id`        | INTEGER  | Chave primária, autoincrementada                |
| `titulo`    | TEXT     | Nome do livro                                   |
| `autor`     | TEXT     | Nome do autor                                   |
| `ano`       | INTEGER  | Ano de lançamento                               |
| `disponivel`| TEXT     | Indica se o livro está disponível ("Sim"/"Não") |

---

## ⚙️ Como usar

### 1. Clone o repositório

```bash
2. Execute o programa principal

Certifique-se de ter o Python instalado. Para rodar o sistema:

python main.py


O terminal exibirá o menu de opções.

📂 Organização do Projeto
biblioteca-online/
│
├── funcoes.py       # Lógica de manipulação do banco de dados
├── main.py          # Interface de linha de comando
└── README.md        # Documentação do projeto

📌 Exemplo de Uso
--------| Biblioteca Online |--------

Digite o número da função que deseja:

1-Listar livros.
2-Cadastrar livro novo.
3-Remover livro já existente.
4-Atualizar disponibilidade do livro.
5-Sair
git clone https://github.com/seuusuario/biblioteca-online.git
cd biblioteca-online
