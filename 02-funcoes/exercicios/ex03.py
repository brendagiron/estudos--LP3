"""
    Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais
    e consoantes na frase.
"""
frase = input('Digite uma frase\n').strip().lower()

def contar(frase):
    vog = 0
    con = 0

    for letra in frase:
        if letra.isalpha():
            if letra in 'aeiou':
                vog +=1
            else:
                con +=1
    return vog, con            

vog, con = contar(frase)
print('tem {} vogais e {} consoantes na frase'.format(vog, con))
