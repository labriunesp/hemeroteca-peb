import os
import sys, subprocess

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
c
    lista_de_pdf = listar_pdfs()
    pdf_tif = pdf_para_tif(lista_de_pdf)
    
    '''for tema in lista_temas:
        pasta_tematica = origem + tema
        for raiz,dirs,pdf in os.walk(pasta_tematica):
            if dirs: # somente lista as pastas temáticas com arquivos pdf.
                print(f'>> A pasta temática {tema.upper()} possui os seguintes arquivos pdf:')
                for sub_dir in dirs:
                    caminho = pasta_tematica + sub_dir + '/'
                    if caminho[-2:] != 'p/': #evitar percorrer as cópias das pastas '_bkp/'
                        lista_pdfs = os.listdir(caminho)
                        for pdf in lista_pdfs:
                            nome = caminho + pdf[:-7]
                            print(nome)'''
                            #args = "'gs','-q','-dNOPAUSE','-r400','-sDEVICE=tiff24nc','-sOutputFile={nome}_page%04d.tif','{nome}.pdf','-c','quit'"
                            #args = f"gs,-q,-dNOPAUSE,-r400,-sDEVICE=tiff24nc,-sOutputFile={nome}_page%04d.tif,{nome}.pdf,-c,quit"
                            #converter = subprocess.call(args.split(','),stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

if __name__ == '__main__':
    main()
