import ocrmypdf
import os, shutil

def fazer_ocr():
    origem = '/media/hdvm08/bd/002/997/001/tif'
    destino = '/media/hdvm08/bd/002/997/001/pdf'
    #ocrmypdf.ocr(origem,destino,deskew=True)
    temas = sorted(os.listdir(origem))[0:-1]
    lista_caminho_origem_tif = []
    for tema in temas:
        lista_caminho_origem_tif.append(f'{origem}/{tema}')
    for caminho_origem_tif, tema in sorted(zip(lista_caminho_origem_tif, temas)):
        for raiz, dirs, arqs in os.walk(caminho_origem_tif):
            for arq in arqs:
                '''if "tif" in arq:
                    #print(arq)
                    cria_destino_tema = os.makedirs(f'{destino_raiz}/{tema}', exist_ok=True)
                    caminho_arq_origem = os.path.join(raiz, arq)
                    #print(caminho_arq_origem)
                    cortar_caminho1 = caminho_arq_origem.split('/')[1:7]
                    cortar_caminho2 = caminho_arq_origem.split('/')[8:]
                    caminho_arq_destino = f"/{'/'.join(cortar_caminho1)}/pdf/{'/'.join(cortar_caminho2)}"
                    #print(f'Caminho_arq_destino = {caminho_arq_destino}')
                    caminho_arq_pdf = f'{caminho_arq_destino[:-4]}.pdf'
                    print(caminho_arq_pdf)'''
            
                pass
                #ocr = ocrmypdf.ocr(f'{raiz}/{arq}',f'{destino}/{tema}/{arq[:-4]}.pdf',deskew=True)
                #destino_tema = os.makedirs(f'{destino}/{tema}', exist_ok=True)
                #copia = shutil.copy2(f'{origem}/{tema},{destino}/{tema}')
    #print(ocr)
    exemplo_destino = '/media/hdvm08/bd/002/997/001/tif/pdfs_nao_pesquisaveis/thiago'
    temas_destino = sorted(os.listdir(exemplo_destino))
    print(temas_destino)
    for raiz, dirs, arqs in sorted(os.walk(exemplo_destino)):   
        for arq in arqs:
            print(arq)
    
            
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
    orc = fazer_ocr()

if __name__=='__main__':
    main()