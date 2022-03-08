def conversor():
    
    #Pendente de tratamento de erros. Farei isso quando tiver um tempo.
    print("Bem vindo ao conversor de temperatura!\n======================================\n")
    
    #Menu de opções simples. Ao digitar a opção, entra na condicional    
    menu = print("Menu de opções: \n================================\n1 - Celsius -> Fahrenheit \n2 - Fahrenheit -> Celsius \n3 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        #Considerando que o valor digitado no input se torna uma string, é importante
        #colocar a instrução "int" antes do input para indicar que tipo de valor deve ser retornado
        temperatura = int(input("\nDigite a temperatura em Celsius: "))
        fahrenheit = (temperatura * 1.8) + 32
        #Aqui tive que converter a variavel em string para que pudesse concatenar no print
        print("A temperatura em Fahrenheit é de " + str(fahrenheit))
    elif opcao == 2:
        temperatura = int(input("\nDigite a temperatura em Fahrenheit: "))
        celsius = (temperatura - 32) / 1.8
        print("A temperatura em Celsius é de " + str(celsius))
    elif opcao == 3:
        print("Você escolheu sair da aplicação. Até a próxima!")
        #retornando o valor False para encerrar a aplicação
        return False

conversor()