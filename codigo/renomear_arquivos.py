from tinydb import TinyDB, Query, where
from time import sleep
import unidecode
import unicodedata
import shutil
import os
# encontrar localização do arquivo
# montar novo nome do arquivo
# renomear arquivo
# atualizar dir_arquivo e nome_arquivo_tif

def consultar_json():
    dir_json = "/media/hdvm08/bd/002/997/001/json/teste10.json"
    db = TinyDB(dir_json,indent=4,ensure_ascii=False)
    buscar = Query()
    for index,i in enumerate(iter(db),start=1):
        data = i["data"]
        sigla = i["jornal_sigla"]
        titulo_noticia = i["titulo_noticia"]
        lista_nome_arquivo_tif = i["nome_arquivo_tif"]
        dir_arquivo = i["dir_arquivo"]
        print(index,titulo_noticia)
        lista_dir_mais_tif = nome_arq_tif(dir_arquivo,lista_nome_arquivo_tif)[0]
        print(lista_dir_mais_tif)
        dir_arq_final = nome_arq_tif(dir_arquivo,lista_nome_arquivo_tif)[1]
        print(dir_arq_final)
        lista_dir_mais_tif_final = sorted(lista_dir_mais_tif)
        if isinstance(titulo_noticia, str):
            titulo = titulo_noticia
        elif isinstance(titulo_noticia, list):
            titulo = titulo_noticia[0]
        if not dir_arquivo == dir_arq_final:
            print("Não está normalizado")
            lista_nome_arquivo_tif = []
            for index,tif in enumerate(lista_dir_mais_tif_final,start=1):
                # 00/00/0000
                nome_arq_data = f'{data[6:]}-{data[3:5]}-{data[0:2]}'
                nome_arq_sigla = sigla
                nome_arq_titulo = unicodedata.normalize("NFD",titulo)
                nome_arq_titulo = nome_arq_titulo.encode("ascii","ignore")
                nome_arq_titulo = nome_arq_titulo.decode("utf-8")
                nome_arq_titulo_final = nome_arq_titulo.replace(" ","_")
                nome_arq_final = f'{nome_arq_data}-{nome_arq_sigla}-{nome_arq_titulo_final}-p{index:02d}.tif'
                lista_nome_arquivo_tif.append(nome_arq_final)
                print(index, nome_arq_final)
                print(tif)
                dir_arq_final_02 = dir_arq_final.replace("/tif/", "/tif3/")
                os.makedirs(dir_arq_final_02, exist_ok=True)
                dir_mais_tif_final = dir_arq_final_02+nome_arq_final
                shutil.move(tif,dir_mais_tif_final)
            db.update_multiple([
            ({"dir_arquivo": dir_arq_final}, ((buscar.titulo_noticia == titulo_noticia) & (buscar.data == data))),
            ({"nome_arquivo_tif": lista_nome_arquivo_tif}, ((buscar.titulo_noticia == titulo_noticia) & (buscar.data == data)))
            ])
        else:
            print("Está normalizado")
           
def dir_arq(dir_arquivo):
    '''
    Responsável por gerar a pasta em que se encontram os arquivos. 
    Ex.: /media/hdvm08/bd/002/997/001/tif/06-brasil-economia_internacional/
    '''
    lista_tmp = dir_arquivo.split('/')
    dir_arq_final = '/'.join(lista_tmp[:-1])+"/"
    return dir_arq_final 

def nome_arq_tif(dir_arquivo,lista_nome_arquivo_tif):
    '''
    Responsável por gerar o caminho completo de cada arquivo tif.
    Ex.: 
    '''
    lista_nome_arq_tif_final = []
    for arq_tif in lista_nome_arquivo_tif:
        dir_arq_final = dir_arq(dir_arquivo)
        dir_mais_tif = dir_arq_final+arq_tif
        lista_nome_arq_tif_final.append(dir_mais_tif)
    return lista_nome_arq_tif_final, dir_arq_final
       


def main():
   consultar_json()

if __name__ == '__main__':
    main()