import os  # biblioteca nativa


"""
- bibliotecas utilizadas para l realizar OCR: layoutparser e o ocrmypdf
"""


def extrair_nome_arquivos():
    pasta = "/home/lantri_rafael/codigo/hemeroteca-peb/exemplos"
    for diretorio, subpastas, arquivos in os.walk(pasta):
        print(f'Diretorio: {diretorio}')
        print(f'Subpastas: {subpastas}')
        print(f'Arquivos: {arquivos}')


def fazer_ocr():
    print("Fazendo OCR da Hemeroteca")


def inserir_metadados():
    print("Inserindo metadados")


def inserir_xmp():
    print("Inserir XMP")


def main():
    ocr = fazer_ocr()
    metadados = inserir_metadados()
    xmp = inserir_xmp()
    ocr = fazer_ocr()
    arquivos = extrair_nome_arquivos()


if __name__ == "__main__":
    main()
