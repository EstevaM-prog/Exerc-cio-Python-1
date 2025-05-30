print ("Cadastro de usuarios") # testo na tela

def login(): # classe de login

    while True:
        username = input("Digite seu usuário: ") # dado para o username do cliente
        password = input("Digite sua senha: ") # dado para senha do cliente

        if (username == "estevam" and password == "123"): # teste de login
            print("Bem-vindo, {}! \n".format(username)) # mensagen de boas vindas
            break  # sai do loop quando acertar
        else:
            print("Por favor, verifique suas credenciais e tente novamente.\n") # mensagen de tentar novamente o login

login()