# Guia sobre try e except em Python

# O que é try e except?
# O bloco try e except é usado para lidar com exceções (erros) em Python.
# Quando um erro ocorre no bloco try, o programa pula para o bloco except,
# permitindo que você trate o erro de maneira controlada e evite que o programa
# seja interrompido inesperadamente.

# Estrutura Básica:
try:
    # Código que pode gerar uma exceção
    pass
except TipoDeErro:
    # Código que será executado se ocorrer a exceção especificada
    pass

# Exemplo 1: Tratando uma exceção genérica
try:
    numero = int(input("Digite um número inteiro: "))
    print("O dobro do número é:", numero * 2)
except:
    print("Erro: Por favor, insira um número válido!")

# Exemplo 2: Tratando exceções específicas
try:
    divisao = 10 / int(input("Digite um número para dividir 10: "))
    print("Resultado da divisão:", divisao)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Erro: Entrada inválida. Digite um número inteiro.")

# Exemplo 3: Usando finally para executar código independente de erros
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:", conteudo)
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
finally:
    print("Execução finalizada.")

# Observação sobre o uso do finally:
# O bloco finally sempre será executado, independentemente de um erro ter ocorrido ou não.

# Exemplo 4: Criando suas próprias exceções
try:
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        raise ValueError("Idade não pode ser negativa!")
    print("Sua idade é:", idade)
except ValueError as e:
    print("Erro:", e)

# Dicas:
# - Sempre que possível, trate exceções específicas para evitar capturar erros não intencionais.
# - Use o bloco finally para liberar recursos, como fechar arquivos ou conexões de banco de dados.
# - Não abuse do except genérico (except:), pois isso pode mascarar erros importantes.
