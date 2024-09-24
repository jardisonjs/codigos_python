eventos = []

while True:
    print("\nEventos agendados:")
    if eventos:
        contador = 1
        for evento in eventos:
            print(f"{contador}. {evento}")
            contador += 1
    else:
        print("Nenhum evento agendado.")

    print("\nOpções:")
    print("1. Adicionar evento")
    print("2. Remover evento")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1, 2, 3): ")

    if opcao == '1':
        novo_evento = input("Digite o nome do novo evento: ")
        eventos += [novo_evento]  
        print(f"Evento '{novo_evento}' adicionado.")
        
    elif opcao == '2':
        if eventos:
            indice = int(input("Digite o número do evento a ser removido: ")) - 1
            if 0 <= indice < contador - 1:  
                evento_removido = eventos[indice]
                eventos = eventos[:indice] + eventos[indice + 1:]  
                print(f"Evento '{evento_removido}' removido.")
            else:
                print("Número de evento inválido.")
        else:
            print("Nenhum evento para remover.")
    
    elif opcao == '3':
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
