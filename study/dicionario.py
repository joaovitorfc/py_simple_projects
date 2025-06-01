# Guia sobre Dicionários em Python

# O que é um Dicionário?
# Um dicionário em Python é uma coleção desordenada de pares chave-valor.
# Cada chave é única e é usada para acessar seu valor correspondente.

# Criando um dicionário
meu_dicionario = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

# Acessando valores
print("Nome:", meu_dicionario["nome"])  # Saída: João
print("Idade:", meu_dicionario["idade"])  # Saída: 25

# Adicionando ou atualizando um par chave-valor
meu_dicionario["profissao"] = "Engenheiro"
meu_dicionario["idade"] = 26  # Atualizando o valor da chave "idade"

# Verificando se uma chave existe
if "cidade" in meu_dicionario:
    print("Cidade encontrada:", meu_dicionario["cidade"])  # Saída: São Paulo

# Removendo um par chave-valor
meu_dicionario.pop("profissao")  # Remove a chave "profissao"
del meu_dicionario["cidade"]  # Outra forma de remover uma chave

# Iterando sobre um dicionário
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")

# Métodos úteis
meu_dicionario.clear()  # Remove todos os elementos do dicionário
copia = meu_dicionario.copy()  # Cria uma cópia do dicionário

# Exemplo 1: Contando palavras em um texto
texto = "banana maçã banana laranja maçã maçã"
contador = {}

for palavra in texto.split():
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

print("Contagem de palavras:", contador)
# Saída: {'banana': 2, 'maçã': 3, 'laranja': 1}

# Exemplo 2: Dicionário aninhado
alunos = {
    "João": {"idade": 20, "curso": "Matemática"},
    "Maria": {"idade": 22, "curso": "Física"},
}

print("Informações de João:", alunos["João"])  # Saída: {'idade': 20, 'curso': 'Matemática'}

# Dicas:
# - Use dicionários quando precisar associar pares chave-valor.
# - Certifique-se de que as chaves sejam únicas e imutáveis (strings, números ou tuplas).
# - Explore métodos como .keys(), .values() e .items() para manipular dicionários de forma eficiente.
