#for 

lista_vendas = [100, 200, 300 ,400]

meta = 400
percentual_bonus = 0.1



for i in range(1): #i é um contador, o range é quantas vezes ele executa o codigo
    print("BCC")

print("----")

#mostra tudo da lista
for item in lista_vendas:  #para cada item dentro da sua lista ... ##tudo vc quer que seja executado varias vezes. 
    print(item)


for venda in lista_vendas:
    if venda >= meta:
        bonus = percentual_bonus * venda

    else:
     bonus=0

    print(bonus)


frutas = ['banana','maça','laranja']

for fruta in frutas:
   print('eu gosto de: ',fruta)






print('--------------')
# FOR em Python: Estrutura de repetição poderosa

# 1. Percorrendo uma lista
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    # Itera sobre cada item da lista 'frutas'
    print("Eu gosto de", fruta)

# 2. Usando for com range()
# Exemplo básico: de 0 a 4
for i in range(5):
    # Itera de 0 até 4 (não inclui 5)
    print("Número:", i)

# Intervalo personalizado: de 2 a 8, pulando de 2 em 2
for i in range(2, 10, 2):
    # Itera de 2 até 8 (não inclui 10), pulando de 2 em 2
    print("Número:", i)

# 3. Percorrendo uma string
palavra = "Python"

for letra in palavra:
    # Itera sobre cada caractere da string 'palavra'
    print("Letra:", letra)

# 4. Iterando com índice e elemento usando enumerate()
frutas = ["maçã", "banana", "laranja"]

for indice, fruta in enumerate(frutas):
    # Retorna o índice e o valor correspondente na lista
    print(f"Fruta {indice}: {fruta}")

# 5. Usando for em listas aninhadas (matriz)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for linha in matriz:
    for elemento in linha:
        # Itera sobre cada elemento das sublistas
        print(elemento, end=" ")
    print()  # Quebra de linha para separar as linhas da matriz

# 6. Usando for com condições
numeros = [1, 2, 3, 4, 5]

for num in numeros:
    if num % 2 == 0:
        # Verifica se o número é par
        print(num, "é par")
    else:
        # Caso contrário, é ímpar
        print(num, "é ímpar")

# 7. Iteração reversa com reversed()
for numero in reversed(range(1, 6)):
    # Itera de forma reversa de 5 a 1
    print(numero)

# Observação:
# Esses exemplos mostram como usar 'for' para iterar sobre diferentes tipos de dados em Python.
