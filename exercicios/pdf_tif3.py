import os
import shutil

def copiar_arq():
    origem = '/media/hdvm08/bd/002/997/001/tif/'
    destino1 = '/media/hdvm08/bd/002/997/001/tif/pdfs_nao_pesquisaveis/'
    for raiz, dirs, arqs in os.walk(origem):  
        for dir in dirs:
            caminho_dir = os.path.join(raiz, dir)
            print(caminho_dir)
            subpastas = caminho_dir.split('/')[8:]
            print(subpastas)
            '''destino2 = os.mkdir(destino1 + '/'.join(subpastas) + '/')
        for arq in arqs:
            if "pdf" in arq:
                caminho_pdfs = os.path.join(raiz,arq)
                copia = shutil.copy2(caminho_pdfs,destino2)
                print(sorted(copia))'''

'''def listar_pdfs():
    origem = '/media/hdvm08/bd/002/997/001/tif/'
    pdfs = []
    for raiz,dirs,arqs in os.walk(origem):
        for arq in arqs:
            if "pdf" in arq:
                caminho_pdfs = os.path.join(raiz, arq)
                pdfs.append(caminho_pdfs)
    return pdfs
    
def copiar_pdfs(lista_de_pdfs):
    for pdf in sorted(lista_de_pdfs):

def copiar_arquivos(lista_de_pdfs):
    for caminho_pdf in sorted(lista_de_pdfs):
        pastas = caminho_pdf.split('/')[8:-2]
        caminho_pastas = '/'.join(pastas) + '/'
        destino = '/media/hdvm08/bd/002/997/001/tif/pdfs_nao_pesquisaveis/'
        dir_destino = destino + caminho_pastas

        caminho_tmp = caminho_pdf.split('/')[:-1]
        caminho_pastas = '/'.join(caminho_tmp) + '/'
        copiar = shutil.copytree(caminho_pastas,dir_destino)
        print(copiar)'''

def main():
    #lista_de_pdfs = listar_pdfs()
    #copiar_pdfs(lista_de_pdfs)
    copiar_arq()

if __name__ == '__main__':
    main()
