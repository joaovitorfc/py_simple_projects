
from funcoes import * 

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
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")



