import os
import shutil
# entrar nas pastas - ok
# retirar '-p01' - ok
# modificar '_p' para '-p' - ok
# incluir ".tif" - ok
# renomear os arquivos da pasta com a modificação


def renomear():
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



def main():
    renomear()

if __name__ == '__main__':
    main()
