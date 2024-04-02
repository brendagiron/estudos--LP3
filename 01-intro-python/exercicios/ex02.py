numero1 = int(input ('digite o primeiro número inteiro'))
numero2 = int(input ('digite o segundo número inteiro'))
numero3 = int(input ('digite o terceiro número inteiro'))



def media_aritmetica(numero1, numero2, numero3):
    media = (numero1 + numero2 + numero3)/3
    print("A média aritmética é:{:.2f}".format(media))


media_aritmetica(numero1, numero2, numero3)    
