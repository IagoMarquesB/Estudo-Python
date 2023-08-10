# ---------------------Loops---------------------
# Loops nos permite iterar sobra qualquer coisa que tenha uma coleção de itens
# Iterado é algo que podemos ir um por um para checar algo na coleção.
# Listas, dicionários, tuples, strings, sets: tudo é iterável

for item in [1, 2, 3, 4, 5]:  # ->Irá printar 2 vezes a variável item para cada index da lista
    print(item)
    print(item)
print("Fim do ciclo")  # -> O valor final de "item" é 5

for item in [1, 2, 3, 4, 5]:  # -> Podemos fazer um loop enlaçado, isto é, um loop dentro de outro
    for x in ["a", "b", "c"]:
        print(item, x)

# Loops em dicionários funcionam de forma levemente diferente

creature = {
    "name": "golem",
    "age": 1000,
    "can swim": False
}

for item in creature:
    print(item)  # -> Isso irá iterar e imprimir apenas as keys

for item in creature.values():
    print(item)  # -> Isso irá iterar e imprimir apenas os valores

for item in creature.items():
    # -> Isso irá iterar e imprimir um touple contendo keys e valores associados
    print(item)
for item in creature.keys():
    print(item)  # -> Isso irá iterar e imprimir as keys

for key, value in creature.items():
    # Faz o unpacking no touple e imprimi a key e o valor sem estar em uma estrutura de dados
    print(key, value)

# ---------------------range---------------------
print(range(0, 100))
# Range é um objeto especial que é uma série numérica no intervalo enviado como argumento do método

# Range tem um terceiro parâmetro, o stepover
for _ in range(0, 10, 2):
    print(_)

for _ in range(10, 0, -1):  # -> Reverter a ordem
    print(_)

# -> Um jeito rápido e fácil de criar listas usando range e loops.
for _ in range(2):
    print(list(range(10)))

# ---------------------enumerate---------------------
# Ele pega um objeto iterável e retorna o index e o valor atrelado
for i, char in enumerate("Pão queijo pão"):
    print(i, char)

for i, char in enumerate([1, 2, 3, 4, 5, 6]):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if i == 50:
        print(i, char)

# ---------------------while loops---------------------
i = 0
while i < 50:
    print(i)
    break  # -> Impede o while loop

while i < 10:
    print(i)
    i += 1
    break  # -> O brek impede o else de ocorrer
else:
    print("Acabou a contagem")

while True:
    responde = input("Say something:\n")
    if (responde == "bye"):
        break

# Break -> Nós saimos do loop
# Continue -> Volta para o loop
# Pass -> Passa para a próxima linha

for item in [1, 2, 3]:
    continue
    # -> Codigo não é acessado por estar depois do continue, que volta para o loop
    print(item)

for item in [1, 2, 3]:
    pass  # -> Impede o erro de ser executado quando não existe nada dentro do loop
