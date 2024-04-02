numero = int(input ('digite um número inteiro'))


ant = 0
sus = 0


def antecessor_num(numero):
    ant = numero -1
    print("Antecessor:{}".format(ant))

def sucessor_num(numero):
    sus = numero +1
    print("Sucessor:{}".format(sus))

antecessor_num(numero)
sucessor_num(numero)
