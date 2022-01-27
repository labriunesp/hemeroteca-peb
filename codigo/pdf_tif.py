import os
import sys, subprocess


def main():
    origem = '/media/hdvm08/bd/002/997/001/tif/02-brasil-america_latina/p3/'
    lista_pdfs = os.listdir(origem)
    print(lista_pdfs)
    lista_temas=[
        '01-Brasil-Africa/',
        '02-brasil-america_latina/',
        '03-brasil-argentina/',
        '04-brasil-asia/',
        '07-brasil-eua/',
        '08-brasil-europa/',
        '12-brasil-politica_exterior/']
    for pdf in lista_pdfs:
        nome = origem + pdf[:-7]
        print(nome)
        #args = "'gs','-q','-dNOPAUSE','-r400','-sDEVICE=tiff24nc','-sOutputFile={nome}_page%04d.tif','{nome}.pdf','-c','quit'"
        #args = f"gs,-q,-dNOPAUSE,-r400,-sDEVICE=tiff24nc,-sOutputFile={nome}_page%04d.tif,{nome}.pdf,-c,quit"
        #converter = subprocess.call(args.split(','),stdout=subprocess.PIPE,stderr=subprocess.STDOUT)


if __name__ == '__main__':
    main()