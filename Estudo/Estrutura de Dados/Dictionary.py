# Dictionary
# É uma estrutura de dados
# Estrutura de dados são uma forma de organizar dados em um container para que esses dados possamm ser utilizados.


dictionary = {
    "a": 1,
    "b": 2
}
print(dictionary["b"])  # ->printa
# Um dicionário tem uma key:value. O  key é um dado imutável e único (string, int,bool) que serve para pegarmos os dados
# Por exemolo, até mesmo um tuple pode ser um key

dictionary_tuple = {
    (1, 2): "Essa key é um tuple",
    (1, 3): "Essa key é outro tuple"
}
print(dictionary_tuple)

# Um dicionario é um par de valores-chaves não ordenados.
# Isto é, eles não estão próximos um ao outro na memória (desordenados)
# Se conhecermos a chave, podemos agarrar os valores atrelados a ela.

other_dictionary = {
    "c": [1, 2, 3],
    "d": "hello",
    "x": True
}  # -> Podemos colocar qualquer valor nos dicionários, inclusive listas
print("LAAAAAAAAAAAAAA")
print(other_dictionary["c"][0]) #Acessa a key C, index 0 da lista
other_dictionary["c"].append(4)
print(other_dictionary["c"][3])

# A mesma coisa pode ser feita com listas

my_list = [
    {
        1: [1, 2, 3],
        "b": [4, 5, 6]

    },
    {
        "c": [7, 8, 9],
        "d": "dados"
    }
]

# -> Agarra o dado do index 0 da lista, de valor 1 index 2 dessa lista
print(my_list[0][1][2])

# O método .get busca o valor do dicionário representado pela key,  e caso não exista, não resulta em um erro
print(dictionary.get('age'))  # -> None.

# O método para saber se uma key existe no dicionário
print("a" in dictionary)  # -> True

# O método para saber se existe um valor no dicionário
print("hello" in dictionary.items())

dictionary2 = dictionary.copy()  # -> Vai copia o dicionário
print(dictionary2)

dictionary2.pop("b")  # -> Remove o key:value
print(dictionary2)

dictionary2.popitem()  # ->Remove o ultimo key:value
print(dictionary2)

dictionary.update({"b": 5})  # -> Atualiza o valor da key b
dictionary.update({"idade": 55})  # -> Adiciona a key:value ao dicionário
print(dictionary)

dictionary.clear()  # -> Isso vai limpar o dicionário
print(dictionary)
