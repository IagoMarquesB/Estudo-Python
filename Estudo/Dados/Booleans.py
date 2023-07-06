# Booleans
# Só existe dois Bool: True e False
Name = "João"
is_cool = False
is_great = True

# Em programação, true e false são 0 e 1. São valores lógicos

print(bool(1))  # -> True
print(bool(0))  # -> False

# Eu posso converter outros valores e dados para booleano, por exemplo

print(bool("Ola"))  # -> True
print(bool(4))  # -> True

# Os valores retornados são verdadeiros, são considerados valores truthy.
# Existem poucos valores considerados falsy, ou seja, que retornam falso, por exemplo:

print(bool(""))  # -> False
print(bool(None))  # -> False
