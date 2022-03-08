def calculaMedia():

    #Pendente de tratamento de erro. Farei isso com calma depois...
    print("\nBem vindo(a) à Calculadora de Média!\n======================================")

    n1 = int(input("Digite a nota do primeiro bimestre: "))
    n2 = int(input("\nDigite a nota do segundo bimestre: "))
    n3 = int(input("\nDigite a nota do terceiro bimestre: "))
    n4 = int(input("\nDigite a nota do quarto bimestre: "))

    media = (n1+n2+n3+n4) / 4

    if media >= 5:
        print("\nSua média final é: "+str(media))
        print("Você foi aprovado!!! :D\n")
    else:
        print("\nSua média final é: "+str(media))
        print("Você foi reprovado! =(\n")

calculaMedia()