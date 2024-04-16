"""
Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.
"""

num = int(input ('Digite um numero\n'))


def tab (num):
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}' )
     
tab(num)