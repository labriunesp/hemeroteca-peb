from tinydb import TinyDB,Query
import os
from time import sleep
import re
#juntar tifs

def gerar_metadados():
    origem = '/media/hdvm08/bd/002/997/001/tif3/'
    for raiz, dirs, arqs in sorted(os.walk(origem)):
        sleep(4)
        for index,arq in enumerate(arqs, start=1):
            print(index, arq)
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
                elif jornal_sigla == "JB-":
                    jornal = "Jornal do Brasil"
                elif jornal_sigla == "SBP":
                    jornal = "Jornal da Ciência"
                elif jornal_sigla == "JC-":
                    jornal = "Jornal do Comércio"
            except:
                jornal = "NA"
            #['1987-03-13-ESP-Brasil_ignora_reuniao_nos_EUA-p01.tif']
            try:
                titulo_noticia = lista_caminho[-1].split("-")[4].replace("_"," ")
                titulo_noticia = re.sub('([a-z,A-Z])', lambda x: x.groups()[0].upper(),titulo_noticia,1).strip()

                print(titulo_noticia)
            except:
                titulo_noticia = "NA"
            nome_arquivo_tif = []
            nome_arquivo_tif.append(arq)
            if 
            arq_tif = arq.split("-")[-2]
            if arq_tif == ""
    
def inserir_bd():
            dir_bd = '/media/hdvm08/bd/002/997/001/json'
            db = TinyDB(f'{dir_bd}/teste12.json', indent = 4, ensure_ascii=False)
            buscar = Query()
            verifica_db = db.contains((buscar.titulo_noticia==titulo_noticia)&(buscar.data==data)&(buscar.nome_arquivo_tif==nome_arquivo_tif))
            if not verifica_db:
                print('Não está na base')
                db.insert({
                    'tema':tema,
                    'data':data,
                    'jornal':jornal,
                    'jornal_sigla': jornal_sigla,
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
    gerar_metadados()

if __name__ == '__main__':
    main()
