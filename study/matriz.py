# Guia sobre Matrizes em Python

# O que é uma Matriz?
# Em Python, uma matriz pode ser representada como uma lista de listas,
# onde cada sublista é uma linha da matriz.

# Exemplo de matriz 3x3:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessando elementos da matriz
print("Elemento na linha 1, coluna 2:", matriz[0][1])  # Saída: 2

# Percorrendo a matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")  # Saída: 1 2 3 4 5 6 7 8 9
    print()

# Adicionando uma linha à matriz
nova_linha = [10, 11, 12]
matriz.append(nova_linha)
print("Matriz com nova linha:", matriz)

# Alterando um elemento
matriz[1][2] = 99  # Altera o elemento na linha 2, coluna 3 para 99
print("Matriz atualizada:", matriz)

# Exemplo 1: Soma de todos os elementos da matriz
soma = 0
for linha in matriz:
    soma += sum(linha)
print("Soma dos elementos da matriz:", soma)

# Exemplo 2: Transposta de uma matriz
transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print("Matriz transposta:", transposta)

# Exemplo 3: Multiplicação de matrizes
A = [
    [1, 2],
    [3, 4]
]
B = [
    [5, 6],
    [7, 8]
]

# Inicializando a matriz resultado com zeros
resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            resultado[i][j] += A[i][k] * B[k][j]

print("Resultado da multiplicação:", resultado)

# Dicas:
# - Use listas de listas para representar matrizes em Python.
# - Para cálculos complexos com matrizes, considere usar bibliotecas como NumPy, que são otimizadas para essas operações.
# - Certifique-se de que as dimensões sejam compatíveis ao realizar operações como soma ou multiplicação de matrizes.
