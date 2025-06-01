#Lista de Palavras:
#Crie uma lista com 5 palavras escolhidas pelo usuário.
#Exiba as palavras em ordem alfabética.
#Remova uma palavra escolhida pelo usuário e exiba a lista atualizada.

# Lista de Palavras


palavras = []
for i in range(5):
    palavra = input(f"Digite a palavra {i+1}: ")
    palavras.append(palavra)

print("\nPalavras em ordem alfabética:")
print(sorted(palavras))  


palavra_remover = input("\nDigite a palavra que deseja remover: ")

if palavra_remover in palavras:
    palavras.remove(palavra_remover)
    print("\nPalavra removida! Lista atualizada:")
    print(palavras)
else:
    print("\nA palavra não está na lista.")
