# Sets
# São coleções(conjuntos) não ordenados de objetos únicos

my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(5)
my_set.add(6)
print(my_set)  # -> Como o set possui valores únicos, o 5 não é adicionado, pois já existia, mas o 6 é adicionado por ser único


# Set não aceita indexidadores, pois os valores são não ordenados
# Se quisemos saber se algo existe, usamos a função in
print(4 in my_set)


my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))  # -> Removemos os duplicados da lista

# Também podemos copiar e limpar sets
new_set = my_set.copy
print(new_set)
my_set.clear()
print(my_set)

# Podemos diferenciar sets
my_set = {1, 2, 3, 4, 5}
your_set = {3, 4, 5, 6, 7, 8, 9}

# -> Busca a diferença entre o primeiro e o segundo
print(my_set.difference(your_set))

my_set.discard(5)  # -> Retira o valor 5 do set
print(my_set)

# -> Atualiza o set para conter apenas a diferença
my_set.difference_update(your_set)
print(my_set)


print(my_set.intersection(your_set))
# -> Mostra a intersecção entre os dois conjuntos sets
# também pode ser feito assim:
print(my_set & your_set)

print(my_set.isdisjoint(your_set))  # -> Pergunta se os sets tem algo em comum

print(my_set.union(your_set))  # -> Une os dois conjuntos sets
# também pode ser feito assim:
print(my_set | your_set)


print(my_set.issubset(your_set))
# -> Pergunta se o conjunto my set está contido no your set


print(my_set.issuperset(your_set))
# -> Pergunta se o conjunto my set contém o your set
