is_magician = True
is_expert = False

# O exercicio é para checar e printar mensagens específicas dependendo dos valores acima

if is_magician & is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("You are a magician, but you need to improve!")
else:
    print("You need magic powers")
