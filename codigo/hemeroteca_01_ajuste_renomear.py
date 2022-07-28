import os
import shutil


def renomear():
    ''' 
     entrar nas pastas
     retirar '-p01' 
     modificar '_p' para '-p' 
     incluir ".tif" 
     renomear os arquivos da pasta com a modificação '''
    origem = '/media/hdvm08/bd/002/997/001/tif3/'
    for raiz, dirs, arqs in sorted(os.walk(origem)):
        for index,arq in enumerate(arqs, start=1):
            dir_arq_arrumar = os.path.join(raiz,arq)
            arq_sem_p01 = arq[:-8]
            arq_com_hifen = list(arq_sem_p01)
            arq_com_hifen[-4] = "-"
            arq_sem_p01 = "".join(arq_com_hifen)+".tif"
            dir_arq_arrumado = os.path.join(raiz,arq_sem_p01)
            renomeação = shutil.move(dir_arq_arrumar,dir_arq_arrumado)
            print(index,renomeação)

def renomear_ajustes():
    '''
    ajustes dos arquivos da pasta tif2
    '''
    origem = '/media/hdvm08/bd/002/997/001/tif2/'
    arq_total = []
    for raiz, dirs, arqs in sorted(os.walk(origem)):
        for index,arq in enumerate(arqs, start=1):
            if "(2)_ti" in arq:
                arq_sem_sufixo = "".join(arq[:-14])+"-p01.tif"
                renomear_sem_sufixo(raiz, arq, arq_sem_sufixo)
                arq_total.append(arq)
            elif "(2)_t" in arq:
                arq_sem_sufixo = "".join(arq[:-13])+"-p01.tif"
                renomear_sem_sufixo(raiz, arq, arq_sem_sufixo)
                arq_total.append(arq)
            elif "(2)-p" in arq:
                arq_sem_sufixo = "".join(arq[:-11])+"-p01.tif"
                renomear_sem_sufixo(raiz, arq, arq_sem_sufixo)
                arq_total.append(arq)
            elif "_2_ti-" in arq:
                arq_sem_sufixo = "".join(arq[:-13])+"-p01.tif"
                renomear_sem_sufixo(raiz, arq, arq_sem_sufixo)
                arq_total.append(arq)
            elif "_2_t-" in arq:
                arq_sem_sufixo = "".join(arq[:-12])+"-p01.tif"
                renomear_sem_sufixo(raiz, arq, arq_sem_sufixo)
                arq_total.append(arq)
            elif "_t-" in arq:
                arq_sem_sufixo = "".join(arq[:-10])+"-p01.tif"
                renomear_sem_sufixo(raiz, arq, arq_sem_sufixo)
                arq_total.append(arq)
            elif "_ti-" in arq:
                arq_sem_sufixo = "".join(arq[:-11])+"-p01.tif"
                renomear_sem_sufixo(raiz, arq, arq_sem_sufixo)
                arq_total.append(arq)
                #TODO
                #renomear títulos com _2_t-
                #_2_ti-
                #_t-
                #_ti-
                #_2_t-
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
    #renomear()
    renomear_ajustes()

if __name__ == '__main__':
    main()
