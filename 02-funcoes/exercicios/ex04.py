"""
Simulador de Eleições: Crie um programa que simule uma votação com três candidatos.O programa deve pedir 
ao usuário para votar várias vezes e, no final, mostrar o número de votos de cada candidato e quem foi 
o vencedor.
"""

def votacao():
    cand1 = 0
    cand2 = 0
    cand3 = 0

    while True:
        
        print(' João - 0')
        print(' Roberta - 1')
        print(' Cleberson - 2')
        print(' Parar votação - 3')

        voto = int(input('Digite o número desejado:\n'))

        if voto == 3:
            result(cand1,cand2, cand3)
            break
        elif voto == 0:
            cand1 += 1
        elif voto == 1:
            cand2 += 1
        elif voto == 2:
            cand3 += 1
        else:
            print('Opção inválida')


def result(cand1, cand2, cand3):
    vencedor = max(cand1, cand2, cand3)


    print('João teve {} votos'.format(cand1))
    print('Roberta teve {} votos'.format(cand2))
    print('Cleberson teve {} votos'.format(cand3))

    print('O resultado da eleição foi:\n')
    if vencedor == cand1:
        print('João ganhou a eleiçao!')
    elif vencedor == cand2:
        print('Roberta ganhou a eleiçao!')
    else:
        print('Cleberson ganhou a eleiçao!')


votacao()

















