while True:
    # Código a ser executado repetidamente
    print("Este loop nunca para por si só.")
    break  # Interrompe o loop


while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        print("Encerrando o programa.")
        break
    elif entrada.isdigit():
        print(f"Você digitou o número: {entrada}")
    else:
        print("Entrada inválida. Tente novamente.")



while True:
    print("\n--- Menu ---")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        print("Você escolheu a Opção 1.")
    elif escolha == "2":
        print("Você escolheu a Opção 2.")
    elif escolha == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")



# Quando usar while True?
# Menus interativos: Onde o usuário escolhe opções até decidir sair.

# Repetições até uma condição externa ser atingida: Como monitorar eventos ou entradas.

# Processos contínuos: Como servidores ou sistemas que só param quando explicitamente encerrados.