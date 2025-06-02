# Guia sobre Funções em Python

# O que é uma função?
# Uma função é um bloco de código reutilizável que executa uma tarefa específica.
# Elas ajudam a organizar o código, evitar repetições e tornam o programa mais modular.

def minha_primeira_funcao():
    """Essa função exibe uma mensagem simples."""
    print("Olá, essa é minha primeira função!")

# Chamando a função
minha_primeira_funcao()

# Parâmetros em funções
# Funções podem receber valores de entrada chamados parâmetros.

def saudacao(nome):
    """Exibe uma mensagem de saudação para o usuário."""
    print(f"Olá, {nome}! Seja bem-vindo!")

# Chamando a função com um argumento
saudacao("João")

# Retornando valores
# Uma função pode devolver um valor usando a palavra-chave return.

def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

resultado = soma(3, 5)
print("A soma é:", resultado)

# Funções com valores padrão
# Você pode definir valores padrão para os parâmetros.

def potencia(base, expoente=2):
    """Retorna a base elevada ao expoente."""
    return base ** expoente

print("2^3:", potencia(2, 3))  # Com expoente definido
print("3^2:", potencia(3))    # Usando o valor padrão

# Argumentos nomeados
# É possível especificar os argumentos pelo nome ao chamar uma função.

def exibir_dados(nome, idade):
    """Exibe o nome e a idade de uma pessoa."""
    print(f"Nome: {nome}, Idade: {idade}")

exibir_dados(idade=25, nome="Ana")

# Funções com número variável de argumentos
# Use *args para receber uma quantidade variável de argumentos.

def somar_todos(*numeros):
    """Retorna a soma de todos os números passados como argumento."""
    return sum(numeros)

print("Soma de 1, 2 e 3:", somar_todos(1, 2, 3))

# Use **kwargs para argumentos nomeados dinâmicos.

def exibir_informacoes(**info):
    """Exibe informações fornecidas como argumentos nomeados."""
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

exibir_informacoes(nome="Carlos", idade=30, cidade="São Paulo")

# Funções anônimas (lambda)
# Uma função lambda é uma função pequena e sem nome.
quadrado = lambda x: x ** 2
print("Quadrado de 4:", quadrado(4))

# Dicas para usar funções:
# 1. Use nomes descritivos para as funções.
# 2. Escreva comentários para explicar o propósito e os parâmetros da função.
# 3. Mantenha as funções curtas e focadas em uma única tarefa.
# 4. Evite efeitos colaterais inesperados, como alterar variáveis globais sem necessidade.
