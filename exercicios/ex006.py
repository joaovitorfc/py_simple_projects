#Exercício Simples: Trabalhando com Números
#Crie uma lista com 3 números informados pelo usuário.

#Exiba os números em ordem crescente.

#Peça ao usuário um número para adicionar à lista.

#Exiba a lista final em ordem crescente.



lista = []
for i in range (3):
    num = int(input(f"digite o n{i+1}:"))
    lista.append(num)

print(f"a sua lista é: {lista}")

lista.sort()
print(f"a sua lista em ordem crescente  é: {lista}")

num_adicionar = int(input("digite um numero para adicionar na lista: "))
lista.append(num_adicionar)
print(f"a sua lista com o número que vc adicionou é: {lista}")

lista.sort()
print(f"a sua lista com o número que vc adicionou e em ordem ordenada é: {lista}")