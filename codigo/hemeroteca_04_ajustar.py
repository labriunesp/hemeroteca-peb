import os
import shutil

# encontrar variações " (-p ", " _1-p " e " _2-p" e retirá-las
# atualizar  "titulo_noticia" e "nome_arquivo_tif"

def ajustar():
    pass

def renomear_ajustes():
    '''
    ajustes dos arquivos da pasta tif
    '''
    origem = '/media/hdvm08/bd/002/997/001/tif/'
    arq_total = []
    for raiz, dirs, arqs in sorted(os.walk(origem)):
        for index,arq in enumerate(arqs, start=1):
            if ("$_1-p" in arq) or ("$_2-p" in arq):
                pass
            elif "(-p" in arq:
                arq_sem_sufixo = "".join(arq[:-9])+arq[-8:]
                #renomear_sem_sufixo(raiz, arq, arq_sem_sufixo)
                print(arq_sem_sufixo)
                print(arq)
                print("###")
                arq_total.append(arq)
            elif "_1-p" in arq:
                arq_sem_sufixo = "".join(arq[:-10])+arq[-8:]
                #renomear_sem_sufixo(raiz, arq, arq_sem_sufixo)
                print(arq_sem_sufixo)
                print(arq)
                print("###")
                arq_total.append(arq)
            elif "_2-p" in arq:
                arq_sem_sufixo = "".join(arq[:-10])+arq[-8:]
                #renomear_sem_sufixo(raiz, arq, arq_sem_sufixo)
                print(arq_sem_sufixo)
                print(arq)
                print("###")
                arq_total.append(arq)
    print(len(arq_total))

def renomear_sem_sufixo(raiz, arq, arq_sem_sufixo):  
    dir_arq_arrumar = os.path.join(raiz,arq)
    dir_arq_arrumado = os.path.join(raiz,arq_sem_sufixo)
    renomeação = shutil.move(dir_arq_arrumar,dir_arq_arrumado)
    print(arq_sem_sufixo)
    print(dir_arq_arrumar)
    print(dir_arq_arrumado)
    print("###")


def main():
    renomear_ajustes()

if __name__ == '__main__':
    main()