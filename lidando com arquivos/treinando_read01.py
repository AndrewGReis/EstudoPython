# %%
nome_arquivo = "historia.txt"
# Abre o arquivo em formato de leitura
open_file = open(nome_arquivo)
# Podemos substituir /\ essa linha de codigo por essa \/
with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)
# Em resumo essas 2 linhas de código(6 e 7)
# Estão executando o que as linhas(4, 15, 19) estão fazendo 
# porém de forma bem mais resumida e automatizada
# %%
# Lê os dados do arquivo
#conteudo = open_file.read()
#print(conteudo)
# %%
# Fecha o arquivo
#open_file.close()
# %%
