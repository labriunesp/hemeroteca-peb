import chardet
import os

def normaliza_encode(origem_caminho_tif):
    #print(origem_caminho_tif, type(origem_caminho_tif))
    try:
        tif_normalizado = chardet.detect(origem_caminho_tif.encode("ascii"))
        tif_normalizado = origem_caminho_tif
    except UnicodeEncodeError as erro:
        erro = str(erro)
        if "'ascii' codec can't encode characters" == erro[:37]:
            try:
                tif_normalizado = origem_caminho_tif.encode('iso-8859-1').decode('utf-8')
                #print(origem_caminho_tif)
                print(tif_normalizado)
                with open('normalizados.txt','a') as arq :
                    arq.write(f'{origem_caminho_tif},{tif_normalizado}')
                    arq.write('\n')
            except:
                tif_normalizado = origem_caminho_tif
                #print(f'Except: {tif_normalizado}')
        else:
            tif_normalizado = origem_caminho_tif
            #print(f'Else: {tif_normalizado}')
    tif_renomeado = os.rename(origem_caminho_tif, tif_normalizado)
    
    return tif_renomeado

def teste():
    arquivos = ['2002-03-26GM-UE_sobretaxa_ao_aÃ§o_entre_14-9_a_26%' , '2002-03-26GM-UE_sobretaxa', '/media/hdvm08/bd/002/997/001/tif/03-brasil-argentina/0000-00-00--argentina_reclama_de_assimetrias_no_comércio_de_carros_com_brasil.tif']
    for arquivo in arquivos:
        print(arquivo)
        try:
            descobrir = chardet.detect(arquivo.encode("ascii"))
            print(descobrir)
        except UnicodeEncodeError as erro:
            erro2 = str(erro)
            print(erro2, type(erro2))
            if "'ascii' codec can't encode characters" == erro2[:37]:
                #print(erro)
                arquivo = arquivo.encode('iso-8859-1').decode('utf-8')
                print(arquivo)

def main():
    #ocr = normaliza_encode()
    ocr = teste()

if __name__=='__main__':
    main()