import datetime
from tinydb import TinyDB,Query



def separar_metadados():
    #[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]
    db = TinyDB('/media/hdvm08/bd/002/997/001/json/teste6.json')
    regex = datetime.datetime.strptime
    for noticia in db:
        try:
            assert regex(noticia['data'], '%d/%m/%Y')
            inserir_bd(noticia,True)
        except ValueError:
            inserir_bd(noticia,False)

def inserir_bd(noticia , metadados):
    dir_bd = '/media/hdvm08/bd/002/997/001/json'
    if metadados == True:
        json = "metadados_bons.json"
    elif metadados == False:
        json = "metadados_ruins.json"
    db = TinyDB(f'{dir_bd}/{json}', indent = 4, ensure_ascii=False)
    buscar = Query()
    dir_arquivo = noticia["dir_arquivo"]
    verifica_db = db.contains((buscar.dir_arquivo==dir_arquivo))
    if not verifica_db:
        print('Não está na base')
        db.insert({
            'tema':noticia["tema"],
            'data':noticia["data"],
            'jornal':noticia["jornal"],
            'jornal_sigla': noticia["jornal_sigla"],
            'titulo_noticia':noticia["titulo_noticia"],
            'nome_arquivo_tif': noticia["nome_arquivo_tif"],
            'nome_arquivo-pdf': noticia["nome_arquivo-pdf"],
            'quant_pages': noticia["quant_pages"],
            'verifica_ocr': noticia["verifica_ocr"],
            'paragrafos': noticia["paragrafos"],
            'autoria': noticia["autoria"],
            'dir_bd': noticia["dir_bd"],
            'dir_arquivo': noticia["dir_arquivo"],
            'codigo_bd': noticia["codigo_bd"],
        })
        #fazer_ocr(origem_caminho_tif)
    else:
        print('JÁ ESTÁ NA BASE')
            
        #print(noticia["titulo_noticia"])
    #if noticia["data"] == 


def main():
    separar_metadados()
    i

if __name__ == '__main__':
    main()