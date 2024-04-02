#for
palavra = 'Python'

for letra in palavra:
    print(letra)


numeros = [1, 2 ,3 ,4, 5 ,6, 8]

for numero in numeros:
    print(numero)

#

for i in range (10):
    print (i)


#while

contador = 0
while contador < 5:
    print(contador)
    contador += 1

#break 
#break pela o loop
#encontrar o numero par

numeros = [1,3,3,4,6]
for numero in numeros:
    if numero %2 == 0:
        print(numero)
    break

#continue
#pula a interação
for numero in numeros:
    if numero <= 0:
        continue
    print(numero)

for numero in numeros:
    if numero > 0:
        print(numero)




#compreensão de lista
 numeros = [2, 3, 4]
 quadrados = [4, 9, 16]

 for numero in numeros:
    quadrados.append(numero**2)


quadrados = [numero ** 2 for numero in numeros]

numeros = [1, 3, 4, 5, 4, 6]
pares = []

for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)


pares = [numero for numero in numeros if numero %2 == 0]

