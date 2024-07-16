#abrir arquivo
arquivo = open ("dados.txt")

print(arquivo)
#print(arquivo.read())

#conteudo = arquivo.read()
#conteudo = arquivo.readlines()
linhas = []
for linha in arquivo:
    linhas.append(linha.strip())

#print(linhas)

#print(conteudo)
#print(conteudo)

arquivo.close()
#arquivo2

#bloco with
with open ("dados.txt", "r") as arquivo2:
    conteudo = arquivo2.read()
    print(conteudo)

#escrever arquivo
#w-substitui td o conteudo
# with open ("dados.txt", "w") as arquivo3:
#     arquivo3.write('FRUTASS')

#a-add nova linha (append)
# with open ("dados.txt", "a") as arquivo4:
#     arquivo4.write('\nFRUTASS')

#ler o arquivo produtos.csv e 
#carregar em memorio uma lista
#na qual cada produto é um dict

def linha_para_produto(linha):
    dados = linha.strip().split(",")
    return {
        'nome': dados[0],
        'descricao': dados[1],
        'preco': float(dados [2]),
        'imagem': dados [3]
    }


# with open("produtos.csv", "r")as arquivo_produtos:
#     produtos = []
#     for linha in arquivo_produtos:
#         produto = linha_para_produto(linha)
#         produtos.append(produto)

#     print(produtos)

def obter_produtos():
    with open("produtos.csv", "r")as arquivo_produtos:
        produtos = []
        for linha in arquivo_produtos:
            produto = linha_para_produto(linha)
            produtos.append(produto)

    return produtos
print(obter_produtos())

def salvar_produtos(nome, descricao, preco, imagem):
    texto = f'\n{nome}, {descricao}, {preco}, {imagem}'
    with open ('produtos.csv', 'a') as arquivo_produtos:
        arquivo_produtos.write(texto)

salvar_produtos('celular', 'tira foto', '1500', 'celular.jpg')



