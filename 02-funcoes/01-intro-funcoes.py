#Função



#Quero somar uma lista de numeros
#Chamar a função sum()

#Quero calcular a media de notas dos dos alunos 
#1 coisa, tem no python?
#2. alguem já programou? (copiar ou add dependencia)
#3. Declarar


#1. Declarar
#def nome_func(parametros):
#     return valor

#nome_func(parametros)



#2. Chamada

print('ola')
sum([1, 2, 3])

#Função sem retorno e sem parametros

def imprimir_mensagem():
    print('Socorrooo!!!')

imprimir_mensagem()
imprimir_mensagem()

#Função sem retorno com parametros
#parametro vs argumentos
def saudacoes(nome):
    print(f'Bom dia {nome}')


#argumento para o parametro nome 'Maria'
saudacoes('Maria')

#argumento para parametro nome
nome_completo = 'jose da silva'
saudacoes(nome_completo)

#parametro é o q ta dentro da função e arumento é que é passado para o parametro, argumentos chamada, parametro definiçao


#Função com retorno e sem parametros

def obter_mensagem():
    return 'Socorro!'

mensagem = obter_mensagem()
print(mensagem)

print(obter_mensagem())


#Função com retorno com argumentos

def gerar_saudacao(nome):
    return f'Bom dia {nome}'

print(gerar_saudacao('Pedro'))
print(gerar_saudacao('João'))

#retorno   parametros
# não         não
# não         sim
# sim         não
# sim         sim    (adequado) (funçao pura)

#imprimir saudacao
#Saudacao = frase (dinamica) nome (dinamico)
#'Bom dia pedro'
#'Boa tarde joao'
#'Boa noite Maria'

def saudacoes(nome, frase):
    print(f'{frase} {nome}')
print('Joao', 'Bom dia')

def saudacoes(nome, frase):
    return(f'{frase} {nome}')

print(saudacoes('Joao', 'Bom dia')) #melhor

#Entrada
todas_as_notas= [
    [9.0, 7.0, 3.0],
    [0.0, 1.0, 3.0],
    [9.0, 7.0, 3.0]
]

#saida [5.5, 1.0, 6.6]

def calcular_media(notas):
    return sum(notas) / len(notas)

def calcular_media_alunos(notas_alunos):
   # medias = []

   # for notas in notas_alunos:
   #     media = calcular_media(notas)
   #     medias.append(media)
    
   # return medias
   return[calcular_media(notas)for notas in notas_alunos]

notas_alunos = [
    [9.0, 7.0, 3.0],
    [0.0, 1.0, 3.0],
    [9.0, 7.0, 3.0]
]

calcular_media_alunos(notas_alunos)

def imprimir_medias(notas_alunos):
    medias = calcular_media_alunos(notas_alunos)
    print(medias)

def enviar_medias_por_email(notas_alunos):
    medias = calcular_media_alunos(notas_alunos)
    #logica de emvar por email as medias

imprimir_medias(todas_as_notas)
enviar_media_por_email(todas_as_notas)

#Argumentos nomeados
def saudacoes(nome, frase):
    return(f'{frase} {nome}')

print(saudacoes('Jose', 'Bom dia')) #não é nomeado

print(saudacoes(nome = 'Jose', frase ='Bom dia')) #nomeado, pode passar os argumentos sem se limitar a ordem dos parametros

print(saudacoes('Jose', frase ='Bom dia')) # da certo

print(saudacoes(nome = 'Jose', 'Bom dia')) # da errado

#Parametros com valor padrao (Default)

def saudacoes(nome, frase = 'Bom dia':
    return(f'{frase} {nome}') # se chamar e não colocar frase ele adota o bom dia como padrao

print(saudacoes('Joao'))
print(saudacoes('Joao', 'Boa tarde'))