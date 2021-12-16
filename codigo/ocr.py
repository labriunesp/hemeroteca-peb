import os
import ocrmypdf

def fazer_ocr():
    origem = '/home/labri_anamota/codigo/hemeroteca-peb/exemplos/tif'
    destino ='/home/labri_anamota/codigo/hemeroteca-peb/exemplos/pdf-pesquisavel'
    for raiz,dirs,files in os.walk(origem):
        for file in files:
            print(f'{file[:-4]}.pdf')
            #ocrmypdf.ocr(f'{origem}/{file}',f'{destino}/{file[:-4]}.pdf',deskew = True)
        


def main():
    fazer_ocr()

if __name__ == '__main__':
    main()