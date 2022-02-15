import ocrmypdf
import os

def fazer_ocr():
    origem_raiz = '/media/hdvm08/bd/002/997/001/tif'
    destino_raiz = '/media/hdvm08/bd/002/997/001/pdf'
    #ocrmypdf.ocr(origem,destino,deskew=True)
    for raiz, dirs, arqs in os.walk(origem_raiz):
        for arq in arqs:
            if "tif" in arq:
                #print(arq)
                origem_caminho_tif = os.path.join(raiz, arq)
                if "02-brasil-america_latina" in origem_caminho_tif: 
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
                        lista_caminho_tifs_erros = []
                        listar_arqs_com_erro = lista_caminho_tifs_erros.append(origem_caminho_tif)
                        continue
    print(listar_arqs_com_erro)

    
def main():
    ocr = fazer_ocr()

if __name__=='__main__':
    main()