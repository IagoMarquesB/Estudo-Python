# Exercicio: Cheque por duplicados em uma lista

some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

# Printe os valores duplicados   OBS: não pode usar sets

duplicate = []

for char in some_list:
    if some_list.count(char) > 1:
        if char not in duplicate:
            duplicate.append(char)
print(duplicate)
