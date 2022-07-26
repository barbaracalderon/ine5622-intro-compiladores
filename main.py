import sys
sys.path.append("../..")

from sintatica import *
from lexica import *


# Leitura do arquivo de dados
def read_data():
    nome_arquivo = input(str('Digite o nome do arquivo de entrada, com a extensão: '))
    with open(nome_arquivo, mode="r", encoding="utf-8") as file:
        dados = file.read()
        return dados


# data = input('Digite seu token: \n')
data = read_data()

analyse_lex(data)

parse(data)
