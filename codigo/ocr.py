from locale import normalize
import ocrmypdf
import os
import re
from tinydb import TinyDB,Query
from normalizar_encode import normaliza_encode


def origem_tif():
    origem_raiz = '/media/hdvm08/bd/002/997/001/tif'
    destino_raiz = '/media/hdvm08/bd/002/997/001/pdf'
    #ocrmypdf.ocr(origem,destino,deskew=True)
    for raiz, dirs, arqs in os.walk(origem_raiz):
        for arq in sorted(arqs):
            if "tif" in arq:
                origem_caminho_tif = os.path.join(raiz, arq)
                if 'page' in arq:
                    nome_arquivo_tif = [x for x in arqs if ('page' in arq) and x.startswith(arq[:-12])] #comprensão de lista
                else:
                    nome_arquivo_tif = [arq]
                #print(nome_arquivo_tif, len(nome_arquivo_tif))
                #print(origem_caminho_tif)
                #tif_normalizado = normaliza_encode(origem_caminho_tif)
                inserir_bd(origem_caminho_tif, nome_arquivo_tif)

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

                
def inserir_bd(origem_caminho_tif, nome_arquivo_tif, nome_arquivo_pdf = "NA", verifica_ocr = "NA"):
    codigo_bd = '/002/997/001'
    print(origem_caminho_tif)
    lista_caminho = origem_caminho_tif.split('/')
    normalizar = lista_caminho[-1].replace("_","-")
    lista_nome_arquivo = normalizar.split('-') 
    #[2010,12,29,ESP,WikiLeaks_põe_Brasil_na_rota_da_droga.tif]
    print(f'lista_nome_arquivo: {lista_nome_arquivo}')
    tema = lista_caminho[-2]
    try:
        data = f'{lista_nome_arquivo[2]}/{lista_nome_arquivo[1]}/{lista_nome_arquivo[0]}'
    except:
        data = 'NA' 
    try:
        if lista_nome_arquivo [3] == '':
            sigla_jornal = 'NA'
        else:
            sigla_jornal = lista_nome_arquivo[3]
    except:
        sigla_jornal = 'NA'
    try:
        if sigla_jornal == "NA":
            nome_jornal = "NA"
        elif sigla_jornal == "ESP":
            nome_jornal = "O Estado de S. Paulo"
        elif sigla_jornal == "FSP":
            nome_jornal = "Folha de S. Paulo"
        elif (sigla_jornal == "GM") or (sigla_jornal == "GZM"):
            nome_jornal = "Gazeta Mercantil"
        else:
            nome_jornal = "NA"
    except:
        nome_jornal = "NA"
    try:
        titulo_noticia = lista_nome_arquivo[4:]
        titulo_noticia = " ".join(titulo_noticia)
        titulo_noticia = titulo_noticia[0:-4].replace('_', " ").replace("  "," ").replace('(1)',"")
        titulo_noticia = re.sub('([a-z,A-Z])', lambda x: x.groups()[0].upper(),titulo_noticia,1).strip()
        if 'page0' in titulo_noticia:
            titulo_noticia = titulo_noticia[:-8].strip()
    except:
        titulo_noticia = 'NA'
    print(f'Data: {data}') 
    print(f'Nome jornal: {sigla_jornal}')
    print(f'Título: {titulo_noticia}')
    dir_bd = '/media/hdvm08/bd/002/997/001/json'
    db = TinyDB(f'{dir_bd}/teste6.json', indent = 4, ensure_ascii=False)
    buscar = Query()
    verifica_db = db.contains((buscar.titulo_noticia==titulo_noticia)&(buscar.data==data))
    if not verifica_db:
        print('Não está na base')
        db.insert({
            'tema':tema,
            'data':data,
            'jornal':nome_jornal,
            'jornal_sigla': sigla_jornal,
            'titulo_noticia':titulo_noticia,
            'nome_arquivo_tif': nome_arquivo_tif,
            'nome_arquivo-pdf': nome_arquivo_pdf,
            'quant_pages': len(nome_arquivo_tif),
            'verifica_ocr': verifica_ocr,
            'paragrafos': "NA",
            'autoria': "NA",
            'dir_bd': dir_bd,
            'dir_arquivo': origem_caminho_tif,
            'codigo_bd': codigo_bd,
        })
        #fazer_ocr(origem_caminho_tif)
    else:
        print('JÁ ESTÁ NA BASE')


def main():
    ocr = origem_tif()

if __name__=='__main__':
    main()