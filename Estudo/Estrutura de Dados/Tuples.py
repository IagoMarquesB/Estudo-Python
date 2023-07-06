# Tuples
# Tuples são como listas imutáveis

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[3])
print(5 in my_tuple)

# Por serem imutáveis, um tuple não pode ser ordenado, revertido etc.
# O tuple pode ser a key de um dicionário por ser imutável

# Eu posso usar slicing em touple também
new_tuple = my_tuple[1:2]  # -> vai do index 1 ao 2. Retorna 2,

# Eu também posso fazer unpacking em um touple
x, y, z, *other = (1, 2, 3, 4, 5, 6, 7)
print(x)
print(y)
print(*other)

# Touple só possui dois métodos:

# count -> conta quantos valores existem no tuple
print(my_tuple.count(5))  # -> 1

# index -> diz qual o index dquele valor do tuple
print(my_tuple.index(3))  # -> 2
