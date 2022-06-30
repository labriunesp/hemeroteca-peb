from tinydb import TinyDB
import os
import glob

def json_consultar(arq_json):
    db = TinyDB(arq_json)
    origem_raiz = '/media/hdvm08/bd/002/997/001/tif3/**'
    lista_tif_json = []
    lista_arq_tifs = []
    for index,noticia in enumerate(iter(db),start=1):
        tif_json = noticia["nome_arquivo_tif"][0]
        lista_tif_json.append(tif_json)
    for arq in glob.iglob(origem_raiz,recursive=True):
        if ".tif" in arq:
            tif = arq.split("/")[-1]
            lista_arq_tifs.append(tif)
    #print(sorted(lista_tif_json))
    print(sorted(lista_arq_tifs))

def main():
    arq_json = '/home/lantri_thiagofernandes/codigo/hemeroteca-peb/json/teste10.json'
    json_consultar(arq_json)

if __name__=='__main__':
    main()