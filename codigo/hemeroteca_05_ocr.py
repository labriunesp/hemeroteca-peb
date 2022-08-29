from locale import normalize
import ocrmypdf
import os
import re
from tinydb import TinyDB,Query
from normalizar_encode import normaliza_encode
from pikepdf import Pdf

# Encontrar os arquivos tifs (ok)
# Passar os arquivos tifs para o ocrmypdf (ok)
# Salvar os arquvios pdfs em uma pasta (ok)
# Verificar língua do ocr
#Continuar da onde parou(ok)
# Unir arquivos pdfs de notícias com mais de uma página (Excluir arquivos individuais)
# Atualizar o banco json indicando que determinado arquvios tem ocr(ok)

def origem_json():
    '''Encontra os arquviso tifs a partir do banco json; Realiza OCR e atualiza a variável NA para "true"''' 
    dir_db = "/home/labri_anamota/codigo/hemeroteca-peb/json/METADADOS_FINAL-bkp2.json"
    db = TinyDB(dir_db,indent = 4, ensure_ascii=False)
    buscar = Query()
    for index,info in enumerate(iter(db),start=1):
        verificar_ocr = info["verifica_ocr"]
        if verificar_ocr == "NA": 
            dir_arquivo = info["dir_arquivo"]
            nome_arquivo_tif = info["nome_arquivo_tif"]
            lista_pdfs = []
            for tif in nome_arquivo_tif:
                arq_tif = dir_arquivo+tif
                ocr = fazer_ocr(arq_tif)
                lista_pdfs.append(ocr)
            merge_pdf(lista_pdfs)
            db.upsert({
                "nome-arquivo_tif":nome_arquivo_tif,
                "verifica_ocr": "true"
                },buscar.nome_arquivo_tif == nome_arquivo_tif)
        elif verificar_ocr == "true":
            print("OCR já foi realizado.")
            

def merge_pdf(lista_pdfs):
    pdf = Pdf.new()
    for tif in lista_pdfs:
        origem = Pdf.open(tif)
        pdf.pages.extend(origem.pages)
    pdf.save(f'{lista_pdfs[-1]}_teste')







def origem_tif():
    ''' Responsável por encontrar os arquivos tifs '''
    origem_raiz = '/media/hdvm08/bd/002/997/001/tif'
    destino_raiz = '/media/hdvm08/bd/002/997/001/pdf'
    for raiz, dirs, arqs in os.walk(origem_raiz):
        for arq in sorted(arqs):
            origem_caminho_tif = f'{raiz}/{arq}'
            print(origem_caminho_tif)
            fazer_ocr(origem_caminho_tif)
            

def fazer_ocr(origem_caminho_tif):
    '''Responsável por fazer o ocr e criar as pastas que contém os arquivos pdf-pesquisáveis'''
    destino_caminho_pdf = origem_caminho_tif.replace('/tif/', '/pdf/').replace('.tif','.pdf')
    print(destino_caminho_pdf)
    destino_lista = destino_caminho_pdf.split("/")[1:-1]
    destino_pasta = f'/{"/".join(destino_lista)}'
    print(destino_lista)
    print(destino_pasta)
    print("###")
    os.makedirs(destino_pasta, exist_ok=True)
    try:
        ocrmypdf.ocr(origem_caminho_tif,destino_caminho_pdf, deskew=True)
    except ocrmypdf.exceptions.DpiError:
            pass
    return destino_caminho_pdf
    

                
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
    #ocr = origem_tif()
    ocr = origem_json()

if __name__=='__main__':
    main()