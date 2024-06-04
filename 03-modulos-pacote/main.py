#importa tudo de matematica
import matematica

print (matematica.PI)
print(matematica.somar(10.0, 3.2))
print(matematica.subtrair(10.0, 3.2))

#importar apenas os elemntos necessarios (constantes, funçoes, classes)

from matematica import PI, subtrair #ideal importar só o que precisa
#from matematica import * /importa tudo

print (PI)
print(subtrair(10.0, 3.2))

#caso tenha conflito de nome
from matematica import PI as PI_MAT, somar, subtrair

PI = 99999

print (PI)
print (PI_MAT)
print(somar(10.0, 3.2))
print(subtrair(10.0, 3.2))

#Importar a função media do pacote estatistica modulo descritiva
from estatistica.descritiva import media
from estatistica.inferencial import VALOR
