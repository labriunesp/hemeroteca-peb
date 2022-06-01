from tinydb import TinyDB, Query, where
from time import sleep
# se não tiver, inserir
def json_conferir():
    dir_json = "/media/hdvm08/bd/002/997/001/json/metadados_final.json"
    db = TinyDB(dir_json,indent=4,ensure_ascii=False)
    dir_json2 = "/media/hdvm08/bd/002/997/001/json/metadados_mesclados_3_bons.json"
    db2 = TinyDB(dir_json2,indent=4,ensure_ascii=False)
    dir_json3 = "/media/hdvm08/bd/002/997/001/json/metadados_verificacao.json"
    db3 = TinyDB(dir_json3,indent=4,ensure_ascii=False)
    buscar = Query()
    #verifica_bd = db.contains((buscar.titulo_noticia == titulo_noticia) & (buscar.quant_pages == quant_pages) & (buscar.data == data))
    for index,t_1 in enumerate(iter(db),start=1):
        titulo = t_1["titulo_noticia"]
        quant_pages = t_1["quant_pages"]
        data = t_1["data"]
        verifica_bd = db2.contains((buscar.titulo_noticia == titulo) & (buscar.quant_pages == quant_pages) & (buscar.data == data))
        print(index, titulo)
        if not verifica_bd:
            print("Não está no metadados_mesclados")
            print('###########')
            sleep(2)
            verifica_bd3 = db3.contains((buscar.titulo_noticia == titulo) & (buscar.quant_pages == quant_pages) & (buscar.data == data))
            if not verifica_bd3:  
                db3.insert({
                    "titulo_noticia": titulo,
                    "data": data,
                    "quant_pages": quant_pages
                })


def main():
   json_conferir() 

if __name__ == '__main__':
    main()