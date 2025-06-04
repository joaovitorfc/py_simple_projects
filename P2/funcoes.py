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

def salvar_em_arquivo(nome_arquivo, lista_filmes):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for filme in lista_filmes:
                arquivo.write(f"Nome: {filme['nome']}\n")
                arquivo.write(f"Duração: {filme['duracao']} minutos\n")
                if "comentario" in filme:
                    arquivo.write(f"Comentário: {filme['comentario']}\n")
                if "nota" in filme:
                    arquivo.write(f"Nota: {filme['nota']}\n")
                arquivo.write("\n")
        print(f"Dados salvos em {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")