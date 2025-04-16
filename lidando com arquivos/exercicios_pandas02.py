#Exercício: Análise de Notas Escolares com Pandas
#Enunciado
#Você é um professor responsável por calcular as médias e verificar a aprovação dos alunos de uma turma. Crie um programa em Python utilizando a biblioteca Pandas que:
#
#Crie um DataFrame com os dados dos alunos contendo:
#
#Nome do aluno
#
#Nota da primeira prova (0-10)
#
#Nota da segunda prova (0-10)
#
#Calcule a média de cada aluno (média aritmética das duas provas)
#
#Adicione uma coluna indicando se o aluno foi aprovado (média ≥ 7)
#
#Filtrar e exibir apenas os alunos aprovados
#
#Exiba o DataFrame final com os alunos aprovados

# %%
import pandas as pd

dados = {
    'nome': ['Ana', 'Carlos', 'João', 'Maria', 'Pedro'],
    'nota_prova1': [8, 5, 6, 7, 9],
    'nota_prova2': [7, 6, 5, 8, 9]
}

df = pd.DataFrame(dados)

df['media'] = (df['nota_prova1'] + df['nota_prova2']) / 2

df['aprovado'] = df['media'] >= 7

alunos_aprovados = df[df['aprovado']]

print(alunos_aprovados)
# %%
