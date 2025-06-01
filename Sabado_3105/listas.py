# Introdução às Listas em Python

# O que são listas?
# Em Python, uma lista é uma coleção ordenada e mutável de itens. Ela pode conter elementos de tipos diferentes.

# Criando listas:
# Uma lista pode ser criada usando colchetes [] ou a função list().
lista_vazia = []
lista_com_elementos = [1, 2, 3, 4, 5]
lista_mista = ["texto", 42, 3.14, True]

# Acessando elementos:
# Você pode acessar elementos individuais da lista usando índices.
# Em Python, os índices começam em 0.
print(lista_com_elementos[0])  # Saída: 1
print(lista_mista[2])         # Saída: 3.14

# Índices negativos permitem acessar elementos de trás para frente.
print(lista_com_elementos[-1])  # Saída: 5

# Modificando elementos:
# Listas são mutáveis, então podemos alterar os valores.
lista_com_elementos[0] = 10
print(lista_com_elementos)  # Saída: [10, 2, 3, 4, 5]

# Adicionando elementos:
# Usamos append() para adicionar um elemento ao final da lista.
lista_com_elementos.append(6)
print(lista_com_elementos)  # Saída: [10, 2, 3, 4, 5, 6]

# Usamos insert() para adicionar um elemento em uma posição específica.
lista_com_elementos.insert(2, 99)
print(lista_com_elementos)  # Saída: [10, 2, 99, 3, 4, 5, 6]

# Removendo elementos:
# Usamos remove() para remover a primeira ocorrência de um elemento.
lista_com_elementos.remove(99)
print(lista_com_elementos)  # Saída: [10, 2, 3, 4, 5, 6]

# Usamos pop() para remover e retornar um elemento por índice (padrão: último).
ultimo = lista_com_elementos.pop()
print(ultimo)                # Saída: 6
print(lista_com_elementos)   # Saída: [10, 2, 3, 4, 5]

# Usamos del para remover um elemento por índice.
del lista_com_elementos[1]
print(lista_com_elementos)  # Saída: [10, 3, 4, 5]

# Usamos clear() para remover todos os elementos da lista.
lista_com_elementos.clear()
print(lista_com_elementos)  # Saída: []

# Outros métodos úteis:
# count() conta a ocorrência de um elemento.
numeros = [1, 2, 3, 2, 1, 2]
print(numeros.count(2))  # Saída: 3

# index() retorna o índice da primeira ocorrência de um elemento.
print(numeros.index(3))  # Saída: 2

# sort() ordena a lista (por padrão, em ordem crescente).
numeros.sort()
print(numeros)  # Saída: [1, 1, 2, 2, 2, 3]

# reverse() inverte a ordem dos elementos na lista.
numeros.reverse()
print(numeros)  # Saída: [3, 2, 2, 2, 1, 1]

# Operações comuns com listas:
# Concatenar listas usando +
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2
print(concatenada)  # Saída: [1, 2, 3, 4, 5, 6]

# Repetir uma lista usando *
repetida = lista1 * 2
print(repetida)  # Saída: [1, 2, 3, 1, 2, 3]

# Verificar se um elemento está na lista usando in
print(3 in lista1)   # Saída: True
print(7 in lista1)   # Saída: False

# Iterar sobre uma lista com um loop for
for elemento in lista2:
    print(elemento)

# Fatiamento de listas:
# Você pode pegar uma parte da lista usando a notação de fatia [inicio:fim:passo].
fatia = concatenada[1:5]  # Pega os elementos do índice 1 ao 4.
print(fatia)              # Saída: [2, 3, 4, 5]

# Exercício:
# 1. Crie uma lista com os números de 1 a 10.
# 2. Adicione o número 11 ao final da lista.
# 3. Remova o número 5.
# 4. Inverta a ordem da lista.
# 5. Exiba a lista final.
