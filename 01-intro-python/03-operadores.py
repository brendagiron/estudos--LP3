#Operadores aritméticos
#+, -, *, /, **
nota1 = 10.0
nota2 = 5.5
nota3 = 7.5

media = (nota1 + nota2 + nota3) / 3

#numeo elevado a outro
#e elevado n
#10 elevado a 2 
numero = 10
numero_elevados_2 = numero * numero
numero_elevados_2 = numero ** 2

#operadores logicos 
#and, or, not
print(True and True)  #true
print(False and True) #false
print(False and False)#false
print(True and False) #false

#or
print(True and True)  #true
print(False and True) #true
print(False and False)#false
print(True and False) #true

#not
print(not True)  #false
print(not False) #true

# permitir a entrada 
# - quando o usuario for funcionario e 
# - o usuario nao estiver bloqueado e 
# - a hora atual estiver entre 8h e 18h 


# permitir entrada
# - admin

usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_admin = False

horario_comercial = hora_atual >= 8 and hora_atual <= 18 
funcionario_ativo = usuario_funcionario and not usuario_bloqueado


if usuario_admin or (funcionario_ativo and horario_comercial):
     print('acesso permitido')


idade = 20
maior_de_idade = idade >= 18

if maior_de_idade:
     pass # ignora o if por enquato

#operadores de comparaçao
#==, !=, >, <, >=, <=

idade = 25
maior_de_idade = idade >= 18


nota1 = 10.0
nota2 = 5.5
nota3 = 7.5

media = (nota1 + nota2 + nota3) / 3

if media >= 6.0:
     print('aprovado')
     pass

#is, is not
# perador de identidade
# compara se os objetos ocupam o mesmo 
#espaço de memoria

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) #true
print(a is b) #false

c = b 
print(b is c) #true

#operador in not in
# verificar se um elemento existe ou não e uma sequencia
#str, çist, tuple

opcoes = ('sim', 'não', 'talvez')
opcao = input ('Digite uma opção')

opcao = opcao.lower()#coloca td em minusculo
opcao = opcao.strip()#tira os espaços 

opcoes = {
     'sim': ['s', 'y', 'yes', 'sim'],
     'não': ['n', 'n', 'no', 'não']
}

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero) # retorna a sequencia


if opcao in opcoes: #retorna boolean
     print('ok')
else:
     print('opção inexistente')


     

