import funcoes 
import os

print("Catalogo de Filmes")
while True:
    print("Escolha uma opção:")
    print("1 - Adicionar filmes assistidos")
    print("2 - Adicionar filmes para assistir")
    print("3 - Exibir listas")
    print("4 - Sair")

    opcao = input("Digite sua escolha: ")


    if opcao == "1":
            funcoes.adicionar_filmes_assistidos()
    elif opcao == "2":
            funcoes.adicionar_filmes_para_assistir()
    elif opcao == "3":
            print("Filmes assistidos:", funcoes.filmes_assistidos)
            print("Filmes para assistir:", funcoes.filme_para_assistir)
    elif opcao == "4":
            os.system("cls")
            print("Programa encerrado.")
            break
    else:
            print("Opção inválida. Tente novamente.")