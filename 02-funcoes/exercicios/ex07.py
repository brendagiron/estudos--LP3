"""
Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta 
(o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra. O usuário tem um número
limitado de tentativas para adivinhar toda a palavra.
"""
def jogo_da_forca():
    oculta = 'rabanada'
   
    def localizar(texto, letra):
        posicoes = []
        for i in range(len(texto)):
            if texto[i] == letra:
                posicoes.append(i)
        return posicoes
   
    print(f'DICA: A palavra tem {len(oculta)} letras')

    tentativa = 0
    pal_secreta = list('_' * len(oculta))
   
    while tentativa <= 10:
        letra_correta = input('Digite somente uma letra: ').lower()    
     
        if letra_correta in oculta:
            print(f'A letra {letra_correta} existe na palavra, parabéns!')                
            posicoes = localizar(oculta, letra_correta)
         
            for i in range(len(pal_secreta)):
                if i in posicoes:
                    pal_secreta[i] = letra_correta  
           
            for char in pal_secreta:  
                print(char, end=' ')
            print()
       
            if '_' not in pal_secreta:  
                print('Parabéns, você ganhou!')
                return
       
        else:
            print(f'A letra {letra_correta} não existe na palavra')
       
        tentativa += 1
   
    print('Você perdeu! A palavra era:', oculta)

jogo_da_forca()