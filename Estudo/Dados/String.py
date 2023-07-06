# String
# String é um pedaço de texto
print(type('Hi, hello, there'))  # -> Podemos usar aspas simples
print(type("Hi, hello, there"))  # -> Ou aspas duplas
print(type("24"))  # -> Pode ser um número
print(type("!"))  # -> Ou um sinal, tudo isso é string

username = "supercoder"  # -> podemos guardar strings em variáveis também
password = "supersecret"

# existe uma outra maneira de trabalhar com string
long_string = '''
WOW
0 0
---
'''

# 3 aspas simples são usadas para long strings, que podem ficar em multiplas linhas
print(long_string)
# ____________________________________________________
# String concatenation
# Concatenar strings é adicionar strings juntas

first_name = "Iago"
last_name = "Marques"
# Podemos juntar strings assim como juntamos os números
full_name = first_name + last_name
print(full_name)
# -> IagoMarques || Para adicionar o espaço, podemos fazer uma mudança
full_name = first_name + " " + last_name
print(full_name)  # -> Iago Marques || Com espaço

# Eu não posso concatenar strings com outros tipos de dados, por exemplo
# print("Ola" + 5)  # -> Isso gera um erro, pois 5 não é uma string.
# ____________________________________________________
# Type Conversion
str(100)  # -isso é uma função, a função string.
# -Quando faço isso, estou convertendo o inteiro 100 em uma string, e portanto, é possivel printa-la.
type(print(str(100)))

# Escape Sequence
# Como aspas e aspas duplas são usadas normalmente em frases
# podemos usar a escape sequence para consertar isso
# Dessa forma, iremos printar as aspas duplas da palavra "kind" sem problemas.
print("It's \"kind\" sunny")
# -> o \t adiciona um espaçamento 'tab' para a string
print("\t It's \"kind\" sunny")
# -> o /n adiciona uma linha, faz o texto pular uma linha.
print("\n It's \"kind\" sunny")

# Formatted Strings
name = "João"
age = 30


# Olá João. Você tem 30 anos :
print("Olá "+name+". Você tem " + str(age)+" anos")
print(f"Ola {name}. Você tem {age} anos")

# Em Python 2:
print("Ola {}. Você tem {} anos".format(name, age))

# String Indexes

random = "La la la"
print(random[0])  # -> L
# [start]    -> O primeiro item é o start
# [start:Stop]   -> Após o : temos o ponto de parada
print(random[2:5])  # -> La
# [start:Stop:stepover]   -> Ele pula o número indicado
print(random[2:5:2])    # -> a
print(random[-1])   # -> O negativo vai de trás pra frente
print(random[::-1])  # -> Isso vai inverter a ordem da string

# Immutability
# As strings são imutáveis, não podem ser mudadas.
# Eu não posso mudar os valores individuais das strings através do index.
# A unica forma de mudar uma string, é colocar um valor totalmente novo para ela.


# Functions
print(len("1234567"))  # -> Calcula o tamanho da string, não começa em 0.

greet = "Olaaaa"
print(greet[:])
print(greet[0:len(greet)])

# Methods
# Métodos são semelhantes a funções, mas pertencem a um grupo
# String Methods

quote = "ser ou não ser"

print(quote.upper())  # -> SER OU NÃO SER
print(quote.capitalize())  # -> Ser ou não ser
print(quote.find("ou"))  # -> Diz a posição index que começa o 'ou'
# -> Troca a primeira sentença pela segunda sem alterar a variável(Lembre-se, strings são imutáveis)
print(quote.replace("ou", "nossa"))

# -> Isso cria uma nova variável com a string trocada
quote2 = quote.replace("ou", "nossa")
