idade = int(input(" Digite sua idade: "))

if idade <= 12:
    print (" Voce e uma Criança")
elif idade == 13:
    print ("Voce e um Adolecente")
elif idade == 14:
    print ("Voce e um Adolecente")
elif idade == 15:
    print ("Voce e um Adolecente")
elif idade == 16:
    print ("Voce e um Adolecente")
elif idade == 17:
    print ("Voce e um Adolecente")
elif idade == 18:
    print ("Voce e um Adulto")
else:
    print (" Voce e maior de idade")

    idade = int(input('Digite sua idade:'))

    if 0 <= idade <= 12:
        print('Você é uma criança')
    elif 13 <= idade <= 18:
        print('Você é um adolescente')
    elif idade >= 18:
        print('Você é um adulto')
    else:
        print('Opção Inválida')