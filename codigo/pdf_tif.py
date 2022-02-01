import os
import sys, subprocess


def main():
    origem = '/media/hdvm08/bd/002/997/001/tif/'
    lista_subdir = os.listdir(origem)
    print(f'O diretório {origem} possui as seguintes pastas temáticas: {lista_subdir}')
    lista_temas=[
        '01-Brasil-Africa/',
        '02-brasil-america_latina/',
        '03-brasil-argentina/',
        '04-brasil-asia/',
        '07-brasil-eua/',
        '08-brasil-europa/',
        '12-brasil-politica_exterior/']
    for tema in lista_temas:
        pasta_tematica = origem + tema
        for raiz,dirs,pdf in os.walk(pasta_tematica):
            if dirs: 
                print(f'>> A pasta temática {tema.upper()} possui os seguintes arquivos pdf:')
                for sub_dir in dirs:
                    caminho = pasta_tematica + sub_dir + '/'
                    if caminho[-2:] != 'p/': #evitar percorrer as cópias das pastas '_bkp/'
                        lista_pdfs = os.listdir(caminho)
                        for pdf in lista_pdfs:
                            nome = caminho + pdf[:-7]
                            print(nome)
                            #args = "'gs','-q','-dNOPAUSE','-r400','-sDEVICE=tiff24nc','-sOutputFile={nome}_page%04d.tif','{nome}.pdf','-c','quit'"
                            #args = f"gs,-q,-dNOPAUSE,-r400,-sDEVICE=tiff24nc,-sOutputFile={nome}_page%04d.tif,{nome}.pdf,-c,quit"
                            #converter = subprocess.call(args.split(','),stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

if __name__ == '__main__':
    main()
