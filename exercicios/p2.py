
filmes_assistidos = []
filme_para_assistir = []

def adicionar_filmes_assistidos():
    while True:
        try:
            nome = input("\nDigite o nome do filme: ")
            duracao = int(input("Digite a duração do filme (em minutos): "))
            comentario = (input("Digite um comentario sobre o filme: "))
            nota = float(input("Digite a nota do filme (entre 0 e 10): "))

            if nota < 0 or nota > 10:
                print("Nota inválida. A nota deve ser entre 0 e 10.")
                continue

          
            filme = {
                "nome": nome,
                "duracao": duracao,
                "comentario": comentario,
                "nota": nota
            }

            
            filmes_assistidos.append(filme)
            print("Filme adicionado com sucesso!")

      
            escolha = input("Você deseja adicionar outro filme? (s/n): ").strip().lower()
            if escolha == "n":
                break

        except ValueError:
            print("Erro! Certifique-se de digitar números válidos para duração e nota.")


def adicionar_filmes_para_assistir():
    while True:
        try:
            nome = input("\nDigite o nome do filme: ")
            duracao = int(input("Digite a duração do filme (em minutos): "))

            filme_não_assistido = {
                "nome": nome,
                "duracao": duracao
            }

            
            filme_para_assistir.append(filme_não_assistido)
            print("Filme adicionado com sucesso!")

            
            escolha = input("Você deseja adicionar outro filme? (s/n): ").strip().lower()
            if escolha == "n":
                break

        except ValueError:
            print("Erro! Certifique-se de digitar um número válido para a duração.")


if __name__ == "__main__":
    print("Bem-vindo ao gerenciador de filmes!")
    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar filmes assistidos")
        print("2 - Adicionar filmes para assistir")
        print("3 - Exibir listas")
        print("4 - Sair")

        opcao = input("Digite sua escolha: ").strip()


        if opcao == "1":
            adicionar_filmes_assistidos()
        elif opcao == "2":
            adicionar_filmes_para_assistir()
        elif opcao == "3":
            print("\nFilmes assistidos:", filmes_assistidos)
            print("Filmes para assistir:", filme_para_assistir)
        elif opcao == "4":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")





