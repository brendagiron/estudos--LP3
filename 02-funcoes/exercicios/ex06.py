"""
Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), converta para 
o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.
"""
pontos = int(input('Digite uma pontuação de 0 a 100: '))

def conversor(pontos):
    
    if pontos >= 90:
        return 'A'
    elif pontos >= 80:
        return 'B'
    elif pontos >= 70:
        return 'C'
    elif pontos >= 60:
        return 'D'
    else:
        return 'F'

def verificaNota(pontos):
    if 0 <= pontos <= 100:
        nota = conversor(pontos)
        print('A pontuação {} para nota é igual a: {}'.format(pontos, nota))
    else:
        print('A pontuação deve estar entre 0 e 100')         
   
conversor(pontos)
verificaNota(pontos)