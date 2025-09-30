import sqlite3
import funcoes as fnc

while True:
    print("""
    --------| Biblioteca Online |--------
        
    Digite o número da função que deseja:

    1-Listar livros.

    2-Cadastrar livro novo.

    3-Remover livro já existente.

    4-Atualizar disponibilidade do livro.

    5-Sair 

    -------------------------------------
    """)
    escolha = int(input("\nDigite um dos números: "))
    try:
        if escolha == 1:
            fnc.listar_livros()

        elif escolha == 2:
            fnc.cadastrar_livro()

        elif escolha == 3:
            fnc.remover_livro()

        elif escolha == 4:
            fnc.disponibilidade()

        elif escolha == 5:
            print("\nMuito obrigado por testar nosso programa\n!")
            break   
    except KeyboardInterrupt:
        print("\nPare de tentar quebrar o código!\n")
    except ValueError:
        print("Por favor digite um número!")
    except Exception as erro:
        print(f"\nPesso perdão pelo erro! ERRO:{erro}\n")