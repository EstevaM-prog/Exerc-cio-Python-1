

print ("Python na Escola de Programação da Alura")



nome = input("Digite seu primeiro nome?")
idade = input(" Digite sua idade?")

# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.'

# Abordagem usando f-string
print (f"Prazer {nome} sua idade é de {idade} anos" )

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))

print ("a")
print ("l")
print ("u")
print ("r")
print ("a")

print('A','L','U','R','A',sep='\n')


pi = 3.14159
print (pi)

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))

