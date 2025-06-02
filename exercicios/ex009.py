#contador = 0
#while (contador < 5):
 #      print(contador)
  #     contador   = contador + 1


#while-else
contador = 0
while (contador < 5):
      print(contador)
      contador = contador + 1
else:
      print("O loop while foi encerrado com sucesso!")

# x = 0
# while x < 10:
  #  print(x)
 #   x += 1
# else:
 #   print("fim while")

x = 0
while x < 10:
    print(x)
    x += 1
    if x == 6:
        print("x é igual a 6")
        break
else:
    print("fim while")