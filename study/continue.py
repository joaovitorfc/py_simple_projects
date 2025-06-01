# Usando 'continue' em Python

# O comando 'continue' é usado para pular a iteração atual de um loop e passar diretamente para a próxima.

# Exemplo 1: Ignorar um número específico em uma lista
numeros = [1, 2, 3, 4, 5]

for num in numeros:
    if num == 3:
        # Pula o número 3
        continue
    print("Número:", num)

# Saída:
# Número: 1
# Número: 2
# Número: 4
# Número: 5

# Exemplo 2: Ignorar números pares
for i in range(1, 11):
    if i % 2 == 0:
        # Pula os números pares
        continue
    print(i)

# Saída:
# 1
# 3
# 5
# 7
# 9

# Exemplo 3: Usando 'continue' em loops aninhados
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0:
            # Pula os números pares
            continue
        print(elemento, end=" ")
    print()  # Quebra de linha após cada linha da matriz

# Saída:
# 1 3
# 5
# 7 9

# Observação:
# O 'continue' é útil para controlar o fluxo de um loop de forma mais precisa.
