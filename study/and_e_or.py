# Operadores AND e OR

temperatura = 95
chuva = "sim"

#se tiver 25 e chovendo
if (temperatura < 25) and (chuva =="sim"):
    print("clima bom!")
else:
    print("não gosto de calor")


a = 10
b = 5

# Verifica se a é maior que 5 e b é maior que 2
resultado = a > 5 and b > 2  # True, porque ambas as condições são verdadeiras
print(resultado)

# Verifica se a é maior que 5 e b é maior que 10
resultado = a > 5 and b > 10  # False, porque a segunda condição é falsa
print(resultado)
