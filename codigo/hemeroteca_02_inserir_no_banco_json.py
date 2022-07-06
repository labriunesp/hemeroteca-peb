from tinydb import TinyDB,Query
import os
#juntar tifs

def inserir_json():
    origem = '/media/hdvm08/bd/002/997/001/tif3/'
    for raiz, dirs, arqs in sorted(os.walk(origem)):
        for index,arq in enumerate(arqs, start=1):
            dir_arq_completo = os.path.join(raiz,arq)
            
    codigo_bd = '/002/997/001'
    #print(origem_caminho_tif)
    lista_caminho = origem_caminho_tif.split('/')
    normalizar = lista_caminho[-1].replace("_","-")
    lista_nome_arquivo = normalizar.split('-') 
    #[2010,12,29,ESP,WikiLeaks_põe_Brasil_na_rota_da_droga.tif]
    #print(f'lista_nome_arquivo: {lista_nome_arquivo}')
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
        elif '_p0' in titulo_noticia:
            titulo_noticia = titulo_noticia[:-4].strip()
    except:
        titulo_noticia = 'NA'
    '''print(f'Data: {data}') 
    print(f'Nome jornal: {sigla_jornal}')'''
    #print(f'Título: {titulo_noticia}')
    dir_bd = '/media/hdvm08/bd/002/997/001/json'
    db = TinyDB(f'{dir_bd}/teste12.json', indent = 4, ensure_ascii=False)
    buscar = Query()
    verifica_db = db.contains((buscar.titulo_noticia==titulo_noticia)&(buscar.data==data)&(buscar.nome_arquivo_tif==nome_arquivo_tif))
    if not verifica_db:
        print('Não está na base')
        db.insert({
            'tema':tema,
            'data':data,
            'jornal':nome_jornal,
            'jornal_sigla': sigla_jornal,
            'titulo_noticia':titulo_noticia,
            'nome_arquivo_tif': nome_arquivo_tif,
            'nome_arquivo-pdf': "NA",
            'quant_pages': len(nome_arquivo_tif),
            'verifica_ocr': "NA",
            'paragrafos': "NA",
            'autoria': "NA",
            'dir_bd': dir_bd,
            'dir_arquivo': origem_caminho_tif,
            'codigo_bd': codigo_bd,
            'extra_01': "NA",
            'extra_02': "NA"
        })
        #fazer_ocr(origem_caminho_tif)
    else:
        print('JÁ ESTÁ NA BASE')
        pass


def main():
    inserir_json()

if __name__ == '__main__':
    main()
