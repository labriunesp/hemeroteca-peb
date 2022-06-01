from tinydb import TinyDB, Query, where
from time import sleep
# encontrar localização do arquivo
# montar novo nome do arquivo
# renomear arquivo
# atualizar dir_arquivo e nome_arquivo_tif


def consultar_json():
    dir_json = "/media/hdvm08/bd/002/997/001/json/metadados_final.json"
    db = TinyDB(dir_json,indent=4,ensure_ascii=False)
    for index,i in enumerate(iter(db),start=1):
        data = i["data"]
        sigla = i["jornal_sigla"]
        titulo_noticia = i["titulo_noticia"]
        lista_nome_arquivo_tif = i["nome_arquivo_tif"]
        dir_arquivo = i["dir_arquivo"]
        print(index,titulo_noticia)
        lista_dir_mais_tif = nome_arq_tif(dir_arquivo,lista_nome_arquivo_tif)
        for tif in lista_dir_mais_tif:
            # criar novo nome do arquivo (data-sigla-titulo_noticia). Obs.: inserir "_" entre as palavras no titulo_noticia
            # renomear o arquivo com o nome acima;
            # atualizar dir_arquivo
            # atualizar lista_nome_arquivo_tif
        #return data, sigla, titulo_noticia, nome_arquivo_tif, dir_arquivo

def dir_arq(dir_arquivo):
    '''
    Responsável por gerar a pasta em que se encontram os arquivos. 
    Ex.: /media/hdvm08/bd/002/997/001/tif/06-brasil-economia_internacional/
    '''
    lista_tmp = dir_arquivo.split('/')
    dir_arq_final = '/'.join(lista_tmp[:-1])+"/"
    print(dir_arq_final)
    print('#####')
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
        dir_mais_tif.append(lista_nome_arq_tif_final)
    return lista_nome_arq_tif_final
       


def main():
   consultar_json()

if __name__ == '__main__':
    main()