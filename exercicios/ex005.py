#Exercício: Gerenciando uma Lista de Números
#Crie uma lista com 5 números inteiros informados pelo usuário.

#Exiba os números em ordem crescente.

#Peça ao usuário um número para adicionar à lista e outro número para remover da lista.

#Exiba a lista final atualizada.

#### Dica para Solução
#Utilize um for para adicionar os 5 números iniciais.

#Use a função sorted() para organizar os números em ordem crescente.

#Para adicionar um número, use append(). Para remover, use remove().




numeros = []
for i in range(5):
    numero = int(input(f"Digite o número {i+1}: "))
    numeros.append(numero)


numeros_crescente = sorted(numeros)  # sorted() retorna uma nova lista ordenada
print("Números em ordem crescente:", numeros_crescente)

num_adicionar= int(input("Adicionar um num: "))
numero_remover = int(input("Digite um número para remover da lista: "))

numeros.append(num_adicionar)

if num_adicionar in numeros:
    numeros.remove(numero_remover)
else:
    print('n ta na lista')

numeros.sort()  # sort() ordena a lista atual
print("\nLista final em ordem crescente:", numeros)