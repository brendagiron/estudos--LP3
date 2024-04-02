
valor = float(input ('digite o valor da compra'))
desconto = 0
valfinal = 0
valdesconto = 0

def desconto(valor):
    if valor < 10:
        desconto = 0
        valdesconto = valor * desconto
        valfinal = valor - valdesconto
        print("O valor final da sua compra agora é:{:.2f}".format(valfinal))


    elif 10 <= valor < 100:
        desconto = 0.05
        valdesconto = valor * desconto
        valfinal = valor - valdesconto
        print("O valor final da sua compra agora é:{:.2f}".format(valfinal))

    elif 10 <= valor <500:
        desconto = 0.10
        valdesconto = valor * desconto
        valfinal = valor - valdesconto
        print("O valor final da sua compra agora é:{:.2f}".format(valfinal))


    else:
        desconto = 0.15
        valdesconto = valor * desconto
        valfinal = valor - valdesconto
        print("O valor final da sua compra agora é:{:.2f}".format(valfinal))

    return valfinal

#chamando a função
desconto(valor)
