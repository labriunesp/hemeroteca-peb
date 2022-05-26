from tinydb import TinyDB, Query, where
from time import sleep

def json_conferir():
    dir_json = "/media/hdvm08/bd/002/997/001/json/metadados_mesclados.json"
    db = TinyDB(dir_json,indent=4,ensure_ascii=False)
    buscar = Query()
    verifica_bd = db.contains((buscar.titulo_noticia == titulo_noticia) & (buscar.quant_pages == quant_pages) & (buscar.data == data))


def main():
   json_conferir() 

if __name__ == '__main__':
    main()