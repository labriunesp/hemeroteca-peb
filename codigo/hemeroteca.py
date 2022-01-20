import os
import ocrmypdf
from dotenv import load_dotenv
'''
    - Indicar localização dos arquivos;
    - Realizar OCR nos arquivos tifs;
    - Extrair nome dos arquivos;
    - Inserir metadados a partir do nome dos arquivos;
    - Transformar arquivos que estão em pdf em tifs (pasta p3);
'''
def diretorios():
    ''' Localiza arquivos '''
    env_dir = load_dotenv('../.env_dir')
    DIR_BD_FINAL = os.getenv('DIR_BD_FINAL')
    print(DIR_BD_FINAL)
    origem = f'{DIR_BD_FINAL}/tif'
    destino = f'{DIR_BD_FINAL}/pdf'
    return origem,destino

def metadados():
    pass

def fazer_ocr():
    origem = diretorios()[0]
    destino = diretorios()[1]
    print(origem)
    for raiz,dirs,files in os.walk(origem):
        if not dirs:
            print(f'A pasta {raiz} não possui subpastas')
        else :
            print(f'A pasta {raiz} possui subpastas')
            for sub_dir in dirs:
                print(sub_dir)
        #for file in files:
            #print(file)
            #print(f'{file[:-4]}.pdf')
            #ocrmypdf.ocr(f'{origem}/{file}',f'{destino}/{file[:-4]}.pdf',deskew = True)
        


def main():
    fazer_ocr()
    #diretorios()

if __name__ == '__main__':
    main()