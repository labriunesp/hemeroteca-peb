from tinydb import TinyDB,Query
import os
#juntar tifs

def inserir_json():
    origem = '/media/hdvm08/bd/002/997/001/tif3/'
    for raiz, dirs, arqs in sorted(os.walk(origem)):
        for index,arq in enumerate(arqs, start=1):
            arq_dir_completo = os.path.join(raiz,arq)
            codigo_bd = '/002/997/001'
            lista_caminho = arq_dir_completo.split('/')
            tema = lista_caminho[8][10:]
            try:
                data_arq = lista_caminho[-1][:10]
                dia = data_arq[-2:]
                mes = data_arq[5:7]
                ano = data_arq[:4]
                data = f'{dia}/{mes}/{ano}'
                print(dia,mes,ano,data)
            except:
                data = "NA"
            try:
                jornal_sigla = lista_caminho[-1][11:14]
                if jornal_sigla == "NA-":
                    jornal_sigla = "NA"
                print(jornal_sigla)
            except:
                jornal_sigla = "NA"
            try:
                if jornal_sigla == "NA-":
                    jornal = "NA"
                elif jornal_sigla == "ESP":
                    jornal = "O Estado de S. Paulo"
                elif jornal_sigla == "FSP":
                    jornal = "Folha de S. Paulo"
                elif jornal_sigla == "GZM":
                    jornal = "Gazeta Mercantil"
                elif jornal_sigla == "GM-":
                    jornal = "Gazeta Mercantil"
                elif jornal_sigla == "VLR":
                    jornal = "Valor Econômico"
                elif jornal_sigla == "JB":
                    jornal = "Jornal do Brasil"
                elif jornal_sigla == "SBP":
                    jornal = "Jornal da Ciência"
                elif jornal_sigla == "JC-":
                    jornal = "Jornal do Comércio"
            except:
                jornal = "NA"
            #['', 'media', 'hdvm08', 'bd', '002', '997', '001', 'tif3', '12-brasil-politica_exterior', '1987-03-13-ESP-Brasil_ignora_reuniao_nos_EUA-p01.tif']
            try:
                #CONTINUAR A PARTIR DAQUI(06/07/2022)
                titulo_noticia = lista_caminho[-1]
            except:
                titulo_noticia = "NA"

    '''
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
        print(f'Data: {data}') 
    print(f'Nome jornal: {sigla_jornal}')
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
        pass'''


def main():
    inserir_json()

if __name__ == '__main__':
    main()
