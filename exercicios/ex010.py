contador = 0
soma = 0

while True:
    numero = float(input("Digite um número (ou 0 para sair): "))

    if numero == 0:
        break

    soma += numero
    contador += 1

media = soma / contador

print("A média dos números digitados é:", media)
