try:
    numero = int(input("digite um numero: "))
    print(numero)
    10/0
except ZeroDivisionError:
    print("Divisão por 0 não é possível")
except ValueError:
    print("digite um valor valido")
except:
    print("erro inesperado")

finally: #independente do que acontecer ele vai executar.
    print("sempre executa")
    