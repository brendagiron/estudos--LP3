"""
 Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique se é um 
 palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma)
"""

palavra = input('Digite uma palavra ou frase\n').lower().strip()

def verificacao(palavra):
    
    inverter = palavra [::-1]
    
    if palavra == inverter:
        print('É um palíndromo')
    else:
        print('Não é um palíndromo')
    
verificacao(palavra)