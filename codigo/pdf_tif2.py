import os
import sys, subprocess
import shutil

def listar_pdfs():
    origem = '/media/hdvm08/bd/002/997/001/tif/'
    pdfs = []
    for raiz,dirs,arqs in os.walk(origem):
        for arq in arqs:
            caminho_pdf = os.path.join(raiz, arq)
            if 'pdf' in caminho_pdf:
                pdfs.append(caminho_pdf)
    return pdfs

def pdf_para_tif(lista_de_pdf):
    for pdf in sorted(lista_de_pdf):
        arq_pdf = pdf[:-4]
        arq = pdf[:-7]
        lista_caminho = arq.split('/')[1:-2]
        destino = '/' + '/'.join(lista_caminho)
        arq_tif = arq.split('/')[-1]
        #args = "'gs','-q','-dNOPAUSE','-r400','-sDEVICE=tiff24nc','-sOutputFile={arquivo}_page%04d.tif','{arquivo}.pdf','-c','quit'"
        args = f"gs,-q,-dNOPAUSE,-r400,-sDEVICE=tiff24nc,-sOutputFile={destino}/{arq_tif}_page%04d.tif,{arq_pdf}.pdf,-c,quit"
        converter = subprocess.call(args.split(','),stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        print(f'{destino}/{arq_tif}')

def move_pdfs_sem_ocr():
    origem = '/media/hdvm08/bd/002/997/001/tif'
    destino = '/media/hdvm08/bd/002/997/001/tif/pdfs_nao_pesquisaveis'
    temas = sorted(os.listdir(origem))[0:-1]
    #print(temas)
    lista_caminho_origem_pdf = []
    for tema in temas:
        lista_caminho_origem_pdf.append(f'{origem}/{tema}')
    #print(lista_caminho_origem_pdf)
    for caminho_origem_pdf, tema in sorted(zip(lista_caminho_origem_pdf, temas)):
        for raiz, dirs, arqs in os.walk(caminho_origem_pdf):
            #print(dirs)
            for arq in arqs:
                if "pdf" in arq:
                    destino_tema = os.makedirs(f'{destino}/{tema}',exist_ok=True)
                    copia_pdf = shutil.copy2(f'{raiz}/{arq}', f'{destino}/{tema}')
                    print(copia_pdf)
                    
                    
                    
       

def main():
    #lista_de_pdf = listar_pdfs()
    #pdf_tif = pdf_para_tif(lista_de_pdf)
    mover_pdfs_sem_ocr = move_pdfs_sem_ocr()

if __name__ == '__main__':
    main()
