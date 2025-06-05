import os 
filmes_assistidos = []
filme_para_assistir = []

def adicionar_filmes_assistidos():
    while True:
        try:
            nome = input("Digite o nome do filme: ")
            duracao = int(input("Digite a duração do filme (em minutos): "))
            comentario = (input("Digite um comentario sobre o filme: "))
            nota = float(input("Digite a nota do filme (entre 0 e 10): "))
            genero = input("Digite o gênero do filme: ")
            lancamento = input("Digite o ano de lançamento do filme: ")
            if nota < 0 or nota > 10:
                print("Nota inválida. A nota deve ser entre 0 e 10.") 
                continue



            filme = {
                "nome": nome,
                "duracao": duracao,
                "comentario": comentario,
                "nota": nota,
                "genero": genero,
                "data de lancamento": lancamento
            }

            filmes_assistidos.append(filme)
            print("Filme adicionado com sucesso!")

            escolha = input("Você deseja adicionar outro filme? (s/n): ")
            if escolha == "n":
                os.system("cls")
                break
            os.system("cls")
        except ValueError:
            print("Erro! Digite números válidos para duração e nota.")




def adicionar_filmes_para_assistir():
    while True:
        try:
            nome = input("Digite o nome do filme: ")
            duracao = int(input("Digite a duração do filme (em minutos): "))

            filme_não_assistido = {
                "nome": nome,
                "duracao": duracao
            }

            
            filme_para_assistir.append(filme_não_assistido)
            print("Filme adicionado com sucesso!")

            
            escolha = input("Você deseja adicionar outro filme? (s/n): ")
            if escolha == "n":
                os.system("cls")
                break
            os.system("cls")
        except ValueError:
            print("Erro! Digite um número válido para a duração.")