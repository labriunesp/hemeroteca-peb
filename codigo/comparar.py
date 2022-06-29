from tinydb import TinyDB
import os


def json_consultar(arq_json):
    db = TinyDB(arq_json)
    origem_raiz = '/media/hdvm08/bd/002/997/001/tif3'
    arquivos = []
    for index,noticia in enumerate(iter(db),start=1):
        tif_json = noticia["nome_arquivo_tif"][0]
        for raiz, dirs, arqs in os.walk(origem_raiz):
            for arq in arqs:
                arquivos.append(arq)
        if tif_json in arquivos:
            #print(index,arq)
            pass
        else:
            #print("TESTE")
            pass
    print(arquivos)

def main():
    arq_json = '/home/lantri_thiagofernandes/codigo/hemeroteca-peb/json/teste10.json'
    json_consultar(arq_json)

if __name__=='__main__':
    main()