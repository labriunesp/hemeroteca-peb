import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz

#TODO:
# identificar similaridade
# excluir arquivo da pasta
# excluir entrada no json

def encontrar_titulos_similares(lista, limite):
    titulos_similares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            similaridade = fuzz.token_set_ratio(lista[i], lista[j])
            if similaridade >= limite:
                print(similaridade)
                print(lista[i])
                print(lista[j])
                print("###")
                titulos_similares.append((lista[i], lista[j], similaridade))
    return titulos_similares


def main():

    dataset = pd.read_json(f'/home/lantri_rafael/codigo/hemeroteca-peb/json/METADADOS_FINAL_copy.json', orient="columns")
    dataset = pd.json_normalize(dataset["METADADOS_FINAL.json"])
    #print(dataset)
    # Filtrar os títulos de notícias com base na similaridade
    lista_titulos = dataset['titulo_noticia'].tolist() 

    titulos_similares = encontrar_titulos_similares(lista_titulos, 85)

    for titulo1, titulo2, similaridade in titulos_similares:
        print(f"Similaridade: {similaridade}%")
        print(f"Título 1: {titulo1}")
        print(f"Título 2: {titulo2}")
        print()

if __name__=='__main__':
    main()