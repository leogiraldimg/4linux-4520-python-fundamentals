# 2 maneiras principais

## open():

# abertura
#                            opções
buffer = open('arquivo.txt', 'rt')
#             path do arquivo

# leitura
# conteudo = buffer.read
conteudo = buffer.readlines()

# adicionar uma linha nova no conteudo
nome = "Giovanni"
idade = "33"
cidade = "Vila dos Remedios"
estado = "SP"

nova_linha = "{};{};{};{}\n".format(nome, idade, cidade, estado)
print(nova_linha)

# conteudo => lista completo do arquivo
# conteudo.append(nova_linha)

# abre novamente um stream...
# arquivo = open('arquivo.txt', 'w')
# arquivo = open('arquivo.txt', 'a')
arquivo = open('novo_arquivo.txt', 'x')

# arquivo.write(string)
arquivo.writelines(conteudo)
# arquivo.writelines([nova_linha])
# arquivo.write(nova_linha)

arquivo.close()

# fechamento
# conteudo.close()
