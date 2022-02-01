import os
import sys, subprocess

def listar_pdfs():
    origem = '/media/hdvm08/bd/002/997/001/tif/'
    pdfs = []
    for raiz,dirs,arqs in os.walk(origem):
        print(sorted(dirs))



def main():
    lista_de_pdf = listar_pdfs()
    
if __name__ == '__main__':
    main()
