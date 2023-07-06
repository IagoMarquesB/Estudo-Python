# Um código que pega o usuário, a senha, e retorna a senha em asterisco junton com a quantidade de algorismos da senha

username = input("Insira seu Username: ")
password = input("Insira sua senha: ")
password_length = len(password)

print(f"{username}, sua senha " + "*"*password_length +
      f" possui {password_length} algarismos")

# Mesma coisa mas talvez mais simples

username = input("Insira seu Username: ")
password = input("Insira sua senha: ")
password_length = len(password)
hidden_password = "*" * password_length

print(f"{username}, sua senha {hidden_password} possui {password_length} algarismos")
