##-----------------------------------TEMPO DE ENTREGA----------------------------------
def nome_restaurante():
    nomeRestaurante = input("Digite o nome do restaurante\n")
    tempoEstimadoEntrega = int(input("Digite o tempo estimado de entrega\n"))

    print(f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos.")

###-----------------------------------Valor do Pedido----------------------------------
def valor_pedido():
    valorHamburguer = float(input())
    quantidadeHamburguer = int(input())
    valorBebida = float(input())
    quantidadeBebida = int(input())
    valorPago = float(input())

    valortotalhamburguer = valorHamburguer * quantidadeHamburguer
    valortotalbebida = valorBebida * quantidadeBebida
    precototal = valortotalbebida + valortotalhamburguer
    troco = valorPago - precototal

    print(f"O preço final do pedido é R$ {precototal:.2f}. Seu troco é R$ {troco:.2f}.")

###-----------------------------------Sobremesa----------------------------------
def sobremesa():
    valorPedido = int(input())

    if valorPedido > 50:
        print("Parabens, você ganhou uma sobremesa gratis!")
    else:
        print("Que pena, você nao ganhou nenhum brinde especial.")

###-----------------------------------Aplicação de Cupom----------------------------------
def cupom():
    def main():
        n = int(input())
        total = 0
        for i in range(1, n + 1):   #Padrão do DIO
            pedido = input().split(" ")
            nome = pedido[0]    #Padrão DIO
            valor = float(pedido[1])
            total += valor
            
        cupom = input()        
        if cupom == "10%":
            valorfinal = total*0.90
            print(f"Valor total: {valorfinal:.2f}")
        elif cupom == "20%":
            valorfinal = total*0.80
            print(f"Valor total: {valorfinal:.2f}")

    if __name__ == "__main__":
        main()

    ##-----------------------------------Identificando pedidos veganos--------------------------

def pedido_vegano():
    numPedidos = int(input())

    for i in range(1, numPedidos + 1):
        prato = input()
        calorias = int(input())
        ehVegano = input()
        if ehVegano == 's':
            print(f"Pedido {i}: {prato} (Vegano) - {calorias} calorias ")
        else:
            print(f"Pedido {i}: {prato} (Nao-vegano) - {calorias} calorias ")
