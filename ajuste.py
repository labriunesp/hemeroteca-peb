import datetime
from tinydb import TinyDB,Query


def ajustar():
    db = TinyDB(f'/home/lantri_rafael/codigo/hemeroteca-peb/metadados_bons.json', indent=4, ensure_ascii=False)
    busca = Query()
    for index, item in enumerate(iter(db), start=1):
        verificar = item["nome_arquivo_tif"][0]
        el = item["nome_arquivo_tif"]
        if "FSP"in verificar:
            print(index, verificar[11:14])
            db.update({"jornal_sigla": "FSP"}, busca.nome_arquivo_tif == el )
            db.update({"jornal": "Folha de S. Paulo"}, busca.nome_arquivo_tif == el )
        elif "ESP" in verificar:
            print(index, verificar[11:18])
            db.update({"jornal_sigla": "ESP"}, busca.nome_arquivo_tif == el )
            db.update({"jornal": "O Estado de S. Paulo"}, busca.nome_arquivo_tif == el )
        elif "ESP" in verificar:
            print(index, verificar[11:18])
            db.update({"jornal_sigla": "ESP"}, busca.nome_arquivo_tif == el )
            db.update({"jornal": "O Estado de S. Paulo"}, busca.nome_arquivo_tif == el )
        elif "ESP" in verificar:
            print(index, verificar[11:18])
            db.update({"jornal_sigla": "ESP"}, busca.nome_arquivo_tif == el )
            db.update({"jornal": "O Estado de S. Paulo"}, busca.nome_arquivo_tif == el )
        elif "GM" in verificar:
            print(index, verificar[11:18])
            db.update({"jornal_sigla": "GM"}, busca.nome_arquivo_tif == el )
            db.update({"jornal": "Gazeta Mercantil"}, busca.nome_arquivo_tif == el )
        elif "GZM" in verificar:
            print(index, verificar[11:18])
            db.update({"jornal_sigla": "GM"}, busca.nome_arquivo_tif == el )
            db.update({"jornal": "Gazeta Mercantil"}, busca.nome_arquivo_tif == el )
        elif "OESP" in verificar:
            print(index, verificar[11:18])
            db.update({"jornal_sigla": "ESP"}, busca.nome_arquivo_tif == el )
            db.update({"jornal": "O Estado de S. Paulo"}, busca.nome_arquivo_tif == el )
        elif "JC" in verificar:
            print(index, verificar[11:18])
            db.update({"jornal_sigla": "JC"}, busca.nome_arquivo_tif == el )
            db.update({"jornal": "Jornal do Comércio"}, busca.nome_arquivo_tif == el )
        elif "JT" in verificar:
            print(index, verificar[11:18])
            db.update({"jornal_sigla": "JT"}, busca.nome_arquivo_tif == el )
            db.update({"jornal": "Jornal da Tarde"}, busca.nome_arquivo_tif == el )
        elif "JB" in verificar:
            print(index, verificar[11:18])
            db.update({"jornal_sigla": "JB"}, busca.nome_arquivo_tif == el )
            db.update({"jornal": "Jornal do Brasil"}, busca.nome_arquivo_tif == el )
        elif "valor" in verificar:
            print(index, verificar[11:18])
            db.update({"jornal_sigla": "VLR"}, busca.nome_arquivo_tif == el )
            db.update({"jornal": "Valor Econômico"}, busca.nome_arquivo_tif == el )
        
        




def main():
    ajustar()

if __name__ == '__main__':
    main()