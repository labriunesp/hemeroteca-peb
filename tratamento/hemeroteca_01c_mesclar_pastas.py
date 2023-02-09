import os
import subprocess
'''
unificaçao dos arquivos nomeados utilizando o padrão DATA-SIGLA_JORNAL-TITULO com os arquivos
 que iniciamente não apresentavam um padrão de nomeacao 
'''
def mesclar_pastas():
    origem = '/media/hdvm08/bd/002/997/001/renomeados/'
    destino = '/media/hdvm08/bd/002/997/001/tif/'
    lista_temas_regiane = [
        '01-Brasil-Africa/',
        '02-brasil-america_latina/',
        '03-brasil-argentina/',
        '04-brasil-asia/',
        '07-brasil-eua/',
        '08-brasil-europa/',
        '12-brasil-politica_exterior/']
    lista_temas_ricardo = os.listdir('/media/hdvm07/bd/002/997/001/Antiga/hemeroteca-peb-metadados/arquivos-renomeados/renomeados')
    #print(lista_temas_ricardo)
    sync_dados = subprocess.call(['rsync','-av',origem,destino])

def main():
    mesclar_pastas()

if __name__ == '__main__':
    main()
