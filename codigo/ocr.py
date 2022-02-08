import ocrmypdf
import os 

def fazer_ocr():
    origem = '/media/hdvm08/bd/002/997/001/tif'
    destino = '/media/hdvm08/bd/002/997/001/pdf'
    #ocrmypdf.ocr (origem,destino,deskew=True)
    for raiz,dirs,arqs in os.walk(origem):
        print(arqs)




def main():
    ocr = fazer_ocr()

if __name__ == '__main__':
    main()