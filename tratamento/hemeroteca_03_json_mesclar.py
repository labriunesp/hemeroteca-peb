from tinydb import TinyDB, Query, where
from time import sleep

'''
script responsavel por unificar o banco json.
metadados 01 estava sem datas e o metadados02 estava com todas as datas corretas,
 então após a correção das datas foi feita a mescla dos bancos json 
'''

def json_consultar(arq_json):
    db = TinyDB(arq_json)
    for index,noticia in enumerate(iter(db),start=1):
        tema = noticia["tema"]
        data = noticia["data"]
        jornal = noticia["jornal"]
        jornal_sigla = noticia["jornal_sigla"]
        titulo_noticia = noticia["titulo_noticia"]
        nome_arquivo_tif = noticia["nome_arquivo_tif"]
        nome_arquivo_pdf = noticia["nome_arquivo_pdf"]
        quant_pages = noticia["quant_pages"]
        verifica_ocr = noticia["verifica_ocr"]
        paragrafos = noticia["paragrafos"]
        autoria = noticia["autoria"]
        dir_bd = noticia["dir_bd"]
        dir_arquivo = noticia["dir_arquivo"]
        codigo_bd = noticia["codigo_bd"]
        print(index,titulo_noticia)
        inserir_db(tema, data, jornal, jornal_sigla,titulo_noticia,nome_arquivo_tif,nome_arquivo_pdf,quant_pages,verifica_ocr,paragrafos,autoria,dir_bd,dir_arquivo,codigo_bd)
        #sleep(2)
        #with open("log.txt","a") as f:
            #titulo = " ".join(titulo_noticia)
            #f.write(titulo + "\n")

def inserir_db(tema, data, jornal, jornal_sigla,titulo_noticia,nome_arquivo_tif,nome_arquivo_pdf,quant_pages,verifica_ocr,paragrafos,autoria,dir_bd,dir_arquivo,codigo_bd):
    dir_json = "/media/hdvm08/bd/002/997/001/json/METADADOS_FINAL.json"
    db = TinyDB(dir_json,indent=4,ensure_ascii=False)
    buscar = Query()
    verifica_bd = db.contains((buscar.titulo_noticia == titulo_noticia) & (buscar.quant_pages == quant_pages) & (buscar.data == data))
    if not verifica_bd:
        print("Não está na base.")
        db.insert({
            "tema" : tema,
            "data" : data,
            "jornal" : jornal,
            "jornal_sigla" : jornal_sigla,
            "titulo_noticia" : titulo_noticia,
            "nome_arquivo_tif" : nome_arquivo_tif,
            "nome_arquivo_pdf" : nome_arquivo_pdf,
            "quant_pages" : quant_pages,
            "verifica_ocr" : verifica_ocr,
            "paragrafos" : paragrafos,
            "autoria" : autoria,
            "dir_bd" : dir_bd,
            "dir_arquivo" : dir_arquivo,
            "codigo_bd" : codigo_bd 
            })
    else:
        print("Já está na base.")

def json_modificar():
    dir_json = "/media/hdvm08/bd/002/997/001/json/METADADOS.json"
    db = TinyDB(dir_json,indent=4,ensure_ascii=False)
    db.update_multiple([
        ({"jornal_sigla": "GZM"}, where("jornal_sigla") == "GM"),
        ({"jornal": "Valor Econômico"}, where("jornal_sigla") == "VLR")
    ])


def main():
    arqs_json = ["/media/hdvm08/bd/002/997/001/json/METADADOS.json", "/media/hdvm08/bd/002/997/001/json/METADADOS02.json"]
    for index,arq_json in enumerate(arqs_json,start=1):
        print(index,arq_json)
        json_consultar(arq_json)

if __name__ == '__main__':
    main()