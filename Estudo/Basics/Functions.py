#Funções

#Função é um bloco de código que recebe um nome, um identificador.
#A função pode ter parâmetros, isto é, a entrada da função.
#A função normalmente retorna um ou mais valor.

def exibir_mensagem():  #-> def informa o interpretador que é uma função
    print("Ola mundo!")

def exibir_mensagem2(nome): #-> Nome é um parâmetro, uma entrada
    print(f"seja bem vindo {nome}!")

def exibir_mensagem3(nome = "Anonimo"): #-> Ao dar um valor ao parâmetro, você cria um caso padrão
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()   #-> É preciso "chamar" a função
exibir_mensagem2("Joao")    #-> estou passando o valor "joão" como parâmetro
exibir_mensagem3()
exibir_mensagem3(nome="Jonas")  #-> Uma outra forma de passar o parâmetro

def calcular_total(numeros):
    return sum(numeros)


print(calcular_total([10,24,32,46]))    #-> Retorna o valor
print(exibir_mensagem3())   #-> Retorna none

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro salvo com sucesso! {marca}/{modelo}/{ano}/{placa}")

#Posso chamar essa função de diferentes maneiras

salvar_carro("Fiat","Palio",1999,"ABC-1234")    #-> Na ordem dos parâmetros
salvar_carro(marca="Fiat", modelo="Palio",ano=1999, placa="ABC-123")    #Argumento nomeado
salvar_carro(**{"marca":"Fiat","modelo":"Palio","ano":1999,"placa":"ABC-123"})  #Como dicionário

#Args e kwargs
#*args -> Os valores são como tupla
#**kwargs -> Os valores são dicionarios, uma estrutura chave - valor
