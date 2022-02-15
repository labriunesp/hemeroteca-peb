import ocrmypdf
import os
from tinydb import TinyDB,Query

def origem_tif():
    origem_raiz = '/media/hdvm08/bd/002/997/001/tif'
    destino_raiz = '/media/hdvm08/bd/002/997/001/pdf'
    #ocrmypdf.ocr(origem,destino,deskew=True)
    for raiz, dirs, arqs in os.walk(origem_raiz):
        for arq in arqs:
            if "tif" in arq:
                #print(arq)
                origem_caminho_tif = os.path.join(raiz, arq)
                inserir_bd(origem_caminho_tif)

def fazer_ocr(origem_caminho_tif):
    if "06-brasil-economia_internacional" in origem_caminho_tif: 
        print(origem_caminho_tif)
        destino_caminho_pdf = origem_caminho_tif.replace('/tif/', '/pdf/').replace('.tif','.pdf')
        print(destino_caminho_pdf)
        tmp_destino_caminho_pdf = destino_caminho_pdf.split('/')[1:-1]
        print(tmp_destino_caminho_pdf)
        destino_caminho_temas = '/'+'/'.join(tmp_destino_caminho_pdf)+'/'
        print(destino_caminho_temas)
        cria_destino_tema = os.makedirs(destino_caminho_temas, exist_ok=True)
        try:
            ocrmypdf.ocr(origem_caminho_tif,destino_caminho_pdf, deskew=True)
        except ocrmypdf.exceptions.DpiError:
                #lista_caminho_tifs_erros = []
                #listar_arqs_com_erro = lista_caminho_tifs_erros.append(origem_caminho_tif)
                pass
    #print(f'## Arquivos com erro: {listar_arqs_com_erro}')

                
def inserir_bd(origem_caminho_tif):
    print(origem_caminho_tif)
    lista_caminho = origem_caminho_tif.split('/')
    nome_arquivo = lista_caminho[-1].split('-')
    print(nome_arquivo)
    tema = lista_caminho[-2]
    try:
        data = f'{nome_arquivo[2]}/{nome_arquivo[1]}/{nome_arquivo[0]}'
    except:
        data = 'NA' 
    try:
        if nome_arquivo[3] == '':
            nome_jornal = 'NA'
        else:
            nome_jornal = nome_arquivo[3]
    except:
        nome_jornal = 'NA'
    try:
        titulo_noticia = '-'.join(nome_arquivo[4:])
    except:
        titulo_noticia = 'NA'
    print(f'Data: {data}') 
    print(f'Nome jornal: {nome_jornal}')
    print(f'Título: {titulo_noticia}')
    db = TinyDB('teste.json', indent = 4, ensure_ascii=False)
    buscar = Query()
    verifica_db = db.contains((buscar.titulo_noticia==titulo_noticia)&(buscar.data==data))
    if not verifica_db:
        print('Não está na base')
        db.insert({
            'tema':tema,
            'data':data,
            'jornal':nome_jornal,
            'titulo_noticia':titulo_noticia,
            'nome_arquivo': lista_caminho[-1]
        })
        #fazer_ocr(origem_caminho_tif)
    else:
        print('JÁ ESTÁ NA BASE')


def main():
    ocr = origem_tif()

if __name__=='__main__':
    main()