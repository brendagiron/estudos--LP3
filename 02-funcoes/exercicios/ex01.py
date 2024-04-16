"""
 Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu
 aleatoriamente. Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.
"""


import random

x = random.randint(1,100)
print(x)

def palpite(x):
    while True:
        num = int(input ('Digite o seu palpite entre 1 e 100\n'))
        
        if num > x:
            print('O palpite está alto')
        elif num < x:
            print('O palpite está baixo')
        else:
            print('O seu palpite está certo')
            break
        
palpite(x)
