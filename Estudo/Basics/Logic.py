# Logica e identação

# Identação é o recuo da linha. Em python, o recuo da linha informa se aquele código pertence a um bloco, de if por exemplo, ou não.

# --------------------- Operadores Lógicos ---------------------

print(4 > 5)  # -> Maior que
print(4 < 5)  # -> Menor que
print(4 == 5)  # -> Igual a
print("Hello" == "Hello")  # -> comparações podem ser feitas com outros dados
print(1 < 2 < 3 < 4)  # -> Multiplas comparações podem ser feitas
print(1 >= 0)  # -> Maior igual
print(0 <= 0)  # -> Menor igual
print(0 != 0)  # -> Diferente que
print(not (True))  # -> Negação lógica
# --------------------- if elif else ---------------------

is_old = True
is_licenced = True

if is_old:  # -> Condicional, faz algo se for verdadeiro. Se for verdadeiro, vai executar todas as ações dentro da identação do if

    print("Você pode dirigir")
elif is_licenced:  # -> É um outro condicional dentro do condicional original, caso o primeiro if seja falso, essa nova condição será feita
    print("Você pode dirigir")
else:  # -> Só roda se o if for falso
    print("Você não pode dirigir")

print("Isso não está dentro do if")

# -> O programa acima não faz sentido, devemos checar as duas condições ao mesmo tempo, e não uma depois da outra.

if is_old and is_licenced:
    print("Você pode dirigir")
else:
    print("Você não pode dirigir")

# -> Esse programa checa as duas condicionais ao mesmo tempo, e funciona da maneira que queremos.

# As comparações não precisam ser necessariamente com valores booleanos

username = "João"
password = "123456"

if password and username:
    print("Esses são valores válidos")
else:
    print("Esses valores não são válidos")

# Caso o username e password tenham valores truthy, eles são valores válidos
# Caso tenham valores falsly, eles são inválidos.

# ---------------------TERNARY OPERATOR#---------------------
# É uma operação que avalia algo com base na condição ser verdadeira ou falsa

# condition_if_true if condition else conditifion_if_else

is_friend = True

can_message = "Troca de mensagens permitida" if is_friend else "Troca de mensagens não permitida"
print(can_message)

# Isso vai atribuir o valor a uma variável dependendo de uma condição
# Se a condição for verdadeira, vai atribuir o primeiro valor, se for falsa, vai atribuir o valor após o else.


# ---------------------Short Circuiting---------------------
is_friend = True
is_user = False

if is_friend or is_user:  # -> Se um valor OU o outro for verdadeiro, a mensagem será printada
    print("Você pode mandar mensagem")

# O programa entra em um "circuito curto" porque ele não precisa ir para a segunda condição caso a primeira já seja verdadeira
# Ou seja, o programa pula uma etapa da checagem que é desnecessária para seu bom funcionamento
