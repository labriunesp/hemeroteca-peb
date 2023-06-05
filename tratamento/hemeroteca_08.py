# data e sigla são iguais
# fazer probabilidade no título para bater os que são iguais
import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from tqdm import tqdm

# Função para calcular a similaridade entre dois títulos
def calcular_similaridade(titulo1, titulo2):
    #print(fuzz.token_set_ratio(titulo1, titulo2))
    return fuzz.token_set_ratio(titulo1, titulo2)

# Função para verificar a similaridade de cada título
def verificar_similaridade(titulo, titulos):
    # Definir a similaridade mínima desejada (80%)
    similaridade_minima = 100
    #print(titulos)
    for outro_titulo in titulos:
        #print(outro_titulo)
        if calcular_similaridade(titulo, outro_titulo) >= similaridade_minima:
            print(titulo)
            print(outro_titulo)
            print("#######")
            return True
    return False

def main():
    dataset = pd.read_json(f'/home/lantri_rafael/codigo/hemeroteca-peb/json/METADADOS_FINAL_copy.json', orient="columns")
    dataset = pd.json_normalize(dataset["METADADOS_FINAL.json"])
    #print(dataset)
    # Filtrar os títulos de notícias com base na similaridade
    titulos_filtrados = dataset['titulo_noticia'].tolist()
    print(titulos_filtrados)
    for titulo in titulos_filtrados:
        verificar_similaridade(titulo, titulos_filtrados)


if __name__=='__main__':
    main()
