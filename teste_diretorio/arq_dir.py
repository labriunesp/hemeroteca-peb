import os
import shutil

def mover_arquivos():
        pasta_origem = ("C:/Users/jcmot/OneDrive/Área de Trabalho/pasta4\\arquivosnovapasta\\teste")
        pasta_destino = "C:/Users/jcmot/OneDrive/Área de Trabalho\pasta4\\arquivospython\\"

        mudar_pasta = os.chdir(pasta_origem)
        listar_arquivos = os.listdir()
        for arquivo in range(1,6):
                cria_arquivo = open(f'{pasta_origem}/teste_{arquivo:02d}.txt','a+')
                with open(f'{pasta_origem}/teste_{arquivo:02d}.txt','a+') as arq:
                        arq.write(f'Teste de escrita {arquivo:02d}\n')
        mover_arquivos = shutil.move(pasta_origem,pasta_destino)
        '''print('%02d'%arquivo) 
        print(f'{arquivo:02d}')
        print('{0:0=2d}'.format(arquivo))'''

        #for file in os.listdir():
               # os.rename(file,pasta_destino + file)
        print(listar_arquivos)

def main():
    mover_arquivos()

if __name__ == '__main__':
    main()