import os, shutil

def move_pdfs_sem_ocr():
    origem = '/media/hdvm08/bd/002/997/001/tif'
    destino = '/media/hdvm08/bd/002/997/001/tif/pdfs_nao_pesquisaveis'
    temas = sorted(os.listdir(origem))[0:-1]
    print(temas)
    lista_caminho_origem_pdf = []
    for tema in temas:
        lista_caminho_origem_pdf.append(f'{origem}/{tema}')
    #print(lista_caminho_origem_pdf)
    for caminho_origem_pdf, tema in sorted(zip(lista_caminho_origem_pdf, temas)):
        for raiz, dirs, arqs in os.walk(caminho_origem_pdf):
            #print(dirs)
            '''for arq in arqs:
                if "pdf" in arq:
                    destino_tema = os.makedirs(f'{destino}/{tema}',exist_ok=True)
                    copia_pdf = shutil.copy2(f'{raiz}/{arq}', f'{destino}/{tema}')
                    print(copia_pdf)'''
                    
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
    move_pdfs_sem_ocr()
    criar_arquivos()


if __name__ == '__main__':
    main()
