# Lists

li = [1, 2, 3, 4, 5, 6, 7]
li2 = ["a", "b", "c"]
li3 = [1, 2, "a", "b", True]  # -> Listas podem ser de tipos mistos

# Data Structure
# Estrutura de dados são uma forma de organizar dados em um container para que esses dados possamm ser utilizados.

amazon_cart = ["Notebook", "óculos", "Livro"]
print(amazon_cart[0])  # -> Acessa o index 0 da lista
print(amazon_cart[2])  # -> Livro

# List slicing
amazon_cart = [
    "Notebook",
    "óculos",
    "Livro",
    "carregador",
    "cabo"
]
# Ao cortar uma lista, estamos criando uma nova lista e não simplesmente copiando a lista antiga
# A diferança de criar uma lista e copia-la, é que a copia corresponde ao endereço de memória
# Portanto, ao mudar o valor de uma lista copiada, o valor será mudado no endereço de memória, afetando a lista original

amazon_copia = amazon_cart
print(f"Essa é a lista nova{amazon_copia}")
print(f"Essa é a lista antiga{amazon_cart}")
amazon_cart[0] = "Chocolate"
# -> O valor 0 da lista original mudou para chocolate, mesmo eu tendo alterado na lista nova
print(f"Essa é a lista antiga {amazon_cart}")

# -> Assim como visto em Strings, podemos cortar a lista
print(amazon_cart[0:2])
print(amazon_cart[1::2])  # -> [start:stop:stepover]

amazon_cart[0] = "CPU"
print(amazon_cart)  # -> Listas são mutáveis, eu posso alterar apenas um membro

# Se quisermos copiar a lista sem copiar seu endereço de memória, devemos criar uma nova lista
# Fazemos isso utilizando slicing


amazon_new = amazon_cart[:]
# -> Isso cria uma nova lista igual a original em um outro endereço de memória.
print(f"Essa é a lista antiga {amazon_cart}")
print(f"Essa é a lista nova{amazon_new}")
amazon_new[0] = "Chocolate"  # -> Eu alterei a nova lista
print(f"Essa é a lista antiga {amazon_cart}")  # -> Mas sem alterar a antiga.
print(f"Essa é a lista nova{amazon_new}")

# Matrix
# Listas bidimensionais

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Podemos ter mais arrays(listas) dentro de arrays

matrix2 = [
    [[1, 2, 3], [9, 8, 7]],
    [4, 5, 6]
]

# -> printa 2. Pega o primeiro array (index 0) e o segundo membro dessa array(index 1)
print(matrix[0][1])

# List Methods
# Existem alguns métodos build-in para listas

print(len(amazon_cart))  # ->Printa o tamanho da lista

# adding

# -> Coloca um novo objeto no final da lista
new_cart = amazon_cart.append("Bolinho")
print(amazon_cart)
# -> Append não produz um valor, ele muda a lista original no local. Por isso o resultado é None
print(new_cart)

# Para gerar uma nova lista com o novo valor, devemos fazer o seguinte
new_cart = amazon_cart  # -> Agora uma nova lista foi gerada
print(new_cart)

# -> Adiciona um novo objeto na lista localmente, no index indicado
amazon_cart.insert(3, "One Piece")
print(amazon_cart)

# -> Adiciona a lista no fim da lista original, também localmente
amazon_cart.extend(["Guaraná", "Caju"])
print(amazon_cart)

# Removing

amazon_cart.pop()  # -> Remove localmente o quer que esteja no final da lista
print(amazon_cart)
# -> Remove o item do index, no caso 0 e retorna o que removeu
amazon_cart.pop(0)
print(amazon_cart)
pop_text = amazon_cart.pop(0)
print(pop_text)  # -> Printa o que foi removido, no caso, óculos


# -> Remove localmente o valor da lista, e não o item do index
amazon_cart.remove("One Piece")
print(amazon_cart)
amazon_cart.clear()  # -> Remove localmente toda a lista.
print(amazon_cart)

# Outros métodos

new_list = [1, 2, 3, 4, 5, 6]
print(new_list.index(3))  # -> Retorna o index do valor 3, no caso 2.
print(new_list.index(2, 0, 3))  # -> Procura entre os index 0 e 3

print("x" in new_list)  # -> Procura se o valor esta na lista
print(3 in new_list)  # -> Procura se o valor esta na lista

print(new_list.count(2))  # -> Retorna quantas vezes o valor se repete na lista

new_list.insert(3, 9)
print(new_list)
new_list.sort()  # -> Organiza a lista localmente
print(new_list)

new_list.insert(3, 10)
print(new_list)

# -> Cria uma cópia da lista e a organiza, mas não altera localmente
print(sorted(new_list))

second_list = new_list.copy()  # ->Copia a lista
print(second_list)

second_list.reverse()  # -> Inverte a lista localmente sem organiza-la
print(second_list)
print(second_list[::-1])  # -> Cria uma nova lista revertida

print(list(range(1, 100)))  # -> Cria uma lista de 1 a 100.
# -> range(start,stop)


# -> Cria uma string com os elementos da lista alternados com os elementos da string original
sentence = "!".join(["ola", "eu", "sou"])
print(sentence)

# List Unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)
# Eu estou retirando valores de uma lista, atribuindo eles a variáveis enquanto mantenho uma parte da lista como uma lista
