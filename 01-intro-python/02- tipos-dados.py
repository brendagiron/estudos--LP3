#tipos de dados
#int, float
#string, list, tuple, set
#dict
#None

#int 
idade = 20
temperatura = 38

#float
altura = 17.15
PI = 3.14

#stringa
nome = 'maria eugenia'
nome = "maria eugenia"

#char
letra = 'a'
letra = 'A'

#é basicamene uma string de um caracter

print(nome[0])
print(nome[-1])

#nome é um objeto da classe string 

print(nome.capitalize())
print(nome)

#interpolação de str e variáveis
#f-string

nome = 'João'
idade = 22
mensagem = f'Olá {nome} você tem {idade} anos'

print(mensagem)

#list
#lista de valores
#pode ser alterada
habilidades = [] #lista vazia
habilidades = ['java', 'c++', 'css'] #lista com valores

print (habilidades[0])
print (habilidades[-1])

habilidades[0] ='javascript' #altera "java"

#tupla
#"lista" de valores 
#não pode ser alterada (adicionar/remover)

opcoes = ('sim', 'não', 'talvez')

#for
for opcao in opcoes:
    print(opcao)

for habilidade in habilidades:
    print(habilidade)


#set
#não indexado
#não permite elementos duplicados
emails = {'maria.com', 'maria.com', 'joao.com'}
emails.add('maria.com')
print(emails)



#dict
#dicionario 
#chave : valor    
#key : value  

#site de emprego
empresa = 'Google'
titulo = 'engenheiro de software'
salario = 2000.00
remoto = False

#vaga
vaga = {

    'empresa': 'Google',
    'titulo': = 'engenheiro de software',
    'salario':= 2000.00,
    'remoto': = False
}

print(vaga['salario'])



#None
nome = None 

def gerar_boletim(prontuario):
    return None

