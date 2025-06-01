# WHILE em Python: Estrutura de repetição condicional

# O 'while' é usado para repetir um bloco de código enquanto uma condição é verdadeira.

# Estrutura básica do 'while':
# while condicao:
#     # Bloco de código a ser executado enquanto a condição for verdadeira

# Exemplo 1: Contagem simples
contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador += 1  # Incrementa o contador para evitar loop infinito

# Saída:
# Contador: 1
# Contador: 2
# Contador: 3
# Contador: 4
# Contador: 5

# Exemplo 2: Pedindo entrada do usuário até uma condição ser satisfeita
senha = "1234"
entrada = ""

while entrada != senha:
    entrada = input("Digite a senha: ")

print("Acesso concedido!")

# Exemplo 3: Uso de 'break' para sair do loop
numero = 1

while True:
    print("Número:", numero)
    if numero >= 5:
        # Interrompe o loop quando a condição é atendida
        break
    numero += 1

# Saída:
# Número: 1
# Número: 2
# Número: 3
# Número: 4
# Número: 5

# Exemplo 4: Uso de 'continue' no while
x = 0

while x < 10:
    x += 1
    if x % 2 == 0:
        # Pula os números pares
        continue
    print("Ímpar:", x)

# Saída:
# Ímpar: 1
# Ímpar: 3
# Ímpar: 5
# Ímpar: 7
# Ímpar: 9

# Observação:
# Certifique-se de que a condição do 'while' eventualmente se torne falsa para evitar loops infinitos.
