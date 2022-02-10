import ocrmypdf
import os, shutil

def fazer_ocr():
    origem_raiz = '/media/hdvm08/bd/002/997/001/tif'
    destino_raiz = '/media/hdvm08/bd/002/997/001/pdf'
    #ocrmypdf.ocr(origem,destino,deskew=True)
    for raiz, dirs, arqs in os.walk(origem_raiz):
        for arq in arqs:
            if "tif" in arq:
                #print(arq)
                origem_caminho_tif = os.path.join(raiz, arq)
                if "01-brasil-africa" or "02-brasil-america_latina" or "03-brasil-argentina" or '04-brasil-asia' or '05-brasil-dialogo_subnacional' or '06-brasil-economia_internacional' in origem_caminho_tif:
                    print(origem_caminho_tif)
                    destino_caminho_pdf = origem_caminho_tif.replace('/tif/', '/pdf/').replace('.tif','.pdf')
                    print(destino_caminho_pdf)
                    tmp_destino_caminho_pdf = destino_caminho_pdf.split('/')[1:-1]
                    print(tmp_destino_caminho_pdf)
                    destino_caminho_temas = '/'+'/'.join(tmp_destino_caminho_pdf)+'/'
                    print(destino_caminho_temas)
                    cria_destino_tema = os.makedirs(destino_caminho_temas, exist_ok=True)
                    ocrmypdf.ocr(origem_caminho_tif,destino_caminho_pdf, deskew=True)

    
                
def criar_arquivos():
    origem = '/media/hdvm08/bd/002/997/001/tif/thiago'
    for arquivo in range(1,6):
        criar_arq = open(f'{origem}/teste_{arquivo:02d}.txt', 'a+') 
        print(criar_arq)
        with open (f'{origem}/teste_{arquivo:02d}.txt', 'a+') as arq:
            arq.write(f'Teste de escrita {arquivo:02d}')    
        #mover_arquivo = shutil.move(origem) 
        #print(mover_arquivo)

def main():
    ocr = fazer_ocr()

if __name__=='__main__':
    main()