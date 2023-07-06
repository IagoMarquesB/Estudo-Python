# Fundamental Data Types
# int and float
print(2 + 4)
# É preciso perfomar uma ação nesses dados.
print(2 - 4)
print(2 * 4)
print(2 / 4)
print("-----------------------------")
print("Estes são os tipos de dados:")
print(type(2 + 4))  # Que tipo de dado é esse? -> <class 'int'>
print(type(2 - 4))  # 'int'
print(type(2 * 4))  # 'int'
print(type(2 / 4))  # 'float'
print("-----------------------------")
# Precisamos de mais memórias para armazenar números floats
# porque precisamos de mais memória para representar o número
# binário antes do ponto, e para representar o número binário depois do ponto.
print(9.9 + 1.1)  # O resultado é 11.0, que é um float
print(type(9.9 + 1.1))
print(2 ** 3)   # 2 elevado a 3
print(5 // 4)  # Essa é uma divisão arredonda para o inteiro mais próximo.
print(5 % 4)  # Mostra o resto da divisão
print("-----------------------------")
# Mathematical Functions
# Functions ou Funções são as ações que pedimos para o computador executar
print(round(3.1))  # Essa função vai arredondar o número para o mais próximo ->3
print(round(3.9))  # Tanto para cima quanto para baixo ->4
print(abs(-20.2))  # Retorna o valor absoluto do número.
# Operator Preference
print(20 - 3 * 4)
# Assim como na matemática, existe uma ordem a ser seguida nos cálculos
# ()
# pow or ** (potenciação)
# Mult e Div ou * /
# + -

print((5 + 4) * 10 / 2)  # -> 9*10/2 -> 90/2 -> 45
print(((5 + 4) * 10) / 2)  # -> (9*10/2) -> 90/2 -> 45
print((5 + 4) * (10 / 2))   # -> 9*5 -> 45
print(5 + (4 * 10) / 2)  # -> 5+40/2 -> 5+20 -> 25
print(5 + 4 * 10 // 2)  # -> 5+ 40//2 -> 5+20 -> 25
