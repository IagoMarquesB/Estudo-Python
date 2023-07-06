# Variáveus guardam informações que podem ser usadas ao longo do programa.
# Variáveis servem para guardar informações no computador

iq = 190    # iq é uma variável que guarda o inteiro 190
# iq é um nome, e 190 está vinculado a esse nome

print(iq)  # Isso printa no console o inteiro 190

# Best Practices Variaveis
# snake_case
# snake_case significa que é tudo letra miniscula, e usamos underline no lugar do espaço
# devem começar com letras minusculas ou underline
# variaveis são case sensitive, isto é, sensiveis a maisculas e minusculas
# variaveis não podem ficar no lugar de palavras chaves da lingua

user_iq = 180  # ->tudo minuscula, underline.
_user_iq = 140  # Isso significa uma variavel privada
user_random = _user_iq/4
print(user_random)

# constantes
# constantes são valores que nunca mudam no programa
PI = 3.14  # Quando criamos uma constante, é usual que colocamos o nome todo em maisculo
# ______________________________________________________
# ______________________________________________________
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
# Essa é uma maneira de guardar valores rapidamente

# Expressions and Statements
iq = 100
user_random = iq/5  # iq/5 é uma expressão porque produz um valor. Uma expresão é uma parte do código que produz um valor

# user_age = iq/5 é um statement é uma instrução, uma linha inteira de código que faz uma ação.

# Augmented Assignment Operator
some_value = 5
some_value = some_value + 2  # -> 7

# Existe uma maneira melhor de fazer isso, usando o Augmented Assignment Operator
some_value += 2  # -> 7
some_value -= 2  # -> 3
# Lembre que o operador vem na esquerda do sinal.
