import numpy as np
import pandas as pd
import json 
import os
from tinydb import TinyDB,Query

def remover_arquivo_repetidos():
    dir_json = "/home/lantri_joaosilva/codigo/hemeroteca-peb/json"
    arq_json_antigo = "METADADOS_ANTIGO.json"
    arq_json_final = "METADADOS_FINAL.json"
    with open (f"{dir_json}/{arq_json_antigo}") as arq:
        j_dataset = json.load(arq)
    
    dataset = pd.read_json(f"{dir_json}/{arq_json_antigo}", orient="columns")
    dataset = pd.json_normalize(dataset["_default"])
    #passar todos os nomes _pdf para caixa baixa
    dataset["nome_arquivo_pdf_lower"] = dataset["nome_arquivo_pdf"].str.lower()
    dataset["nome_arquivo_pdf_lower"]
    #mostrar apenas os arquivos duplicados
    duplicadas = dataset[dataset["nome_arquivo_pdf_lower"].duplicated(keep = False)]
    duplicadas.shape
    #selecionar as noticias que serão mantidas
    duplicadas["contar_caixa_alta"] = duplicadas["nome_arquivo_pdf"].str.count(r"[A-Z]")
    mais_caixa_alta = duplicadas.groupby("nome_arquivo_pdf_lower")["contar_caixa_alta"].idxmax()
    selecionadas = duplicadas.loc[mais_caixa_alta]
    selecionadas
    #noticias que serão excluidas
    nao_selecionadas = duplicadas[~duplicadas.index.isin(selecionadas.index)]
    nao_selecionadas.shape
    #lista com o caminho completo dos arquivos pdf que serão excluidos
    nao_selecionadas["caminho_pdf"] = nao_selecionadas["dir_pdf"]+"/"+nao_selecionadas["nome_arquivo_pdf"]
    lista_caminho_pdf_excluir = nao_selecionadas["caminho_pdf"].tolist()
   
    #lista com o caminho completo dos arquivos tif que serão excluidos
    nao_selecionadas["caminho_arquivo_tif"] = nao_selecionadas.apply(lambda linha: [linha["dir_arquivo"]+tif for tif in linha["nome_arquivo_tif"] ],axis=1 )
    nao_selecionadas = nao_selecionadas.explode("caminho_arquivo_tif")
    nao_selecionadas = nao_selecionadas[["dir_arquivo","caminho_arquivo_tif"]]
    lista_caminho_tif_excluir = nao_selecionadas["caminho_arquivo_tif"].tolist()
    
    #dataframe sem as entradas repetidas
    novo_dataset = dataset.drop(nao_selecionadas.index)
    novo_dataset.shape

    novo_dataset_dict = novo_dataset.to_dict(orient="records")
    db = TinyDB(f"{dir_json}/{arq_json_final}",indent=4,ensure_ascii=False)
    #novo_dataset_json = pd.read_json(f"{dir_json}/{arq_json_final}",convert_axes=False) 
    tabela = db.table("METADADOS_FINAL.json")
    tabela.insert_multiple(novo_dataset_dict)   

    
    excluir_arquivos(lista_caminho_tif_excluir)
    excluir_arquivos(lista_caminho_pdf_excluir)
    db.close()

def excluir_arquivos(lista_arquivos):
    for arquivo in lista_arquivos:
        if os.path.exists(arquivo):
            os.remove(arquivo)

def main():
    remover = remover_arquivo_repetidos()

if __name__=='__main__':
    main()