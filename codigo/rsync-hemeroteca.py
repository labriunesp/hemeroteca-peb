import subprocess

def sync_hemeroteca():
    dir_base='/media/hdvm07/bd/002/997/001'
    dir_antigo='/Antiga/hemeroteca-peb-metadados/00-estrutura_de_pasta_nova-ARRUMADO-TIFF'
    dir_regiane='/H-regiane_com_ST-crop-marca-page_SEPARADOS-ARRUMADO/'
    dir_origem=dir_base+dir_antigo+dir_regiane
    dir_destino='/media/hdvm08/bd/002/997/001'
    lista_temas=[
        '01-Brasil-Africa/',
        '02-brasil-america_latina/',
        '03-brasil-argentina/',
        '04-brasil-asia/',
        '07-brasil-eua/',
        '08-brasil-europa/',
        '12-brasil-politica_exterior/']
    for tema in lista_temas:
        origem = dir_origem + tema
        destino = dir_destino + '/tif/' + tema
        #sync_dados = sysrsync.run(source=origem,destination=destino,options=['-a','-v'])
        sync_dados = subprocess.call(['rsync','-av',origem,destino])
        #sync_dados = subprocess.call(f"rsync -av {origem} {destino}".split())

def main():
    sync_hemeroteca()

if __name__ == '__main__':
    main()  