from pikepdf import Pdf
from tinydb import TinyDB,Query 
from PyPDF2 import PdfReader, PdfWriter
from typing_extensions import TypeAlias

# consultar a base json (pegar o caminho do arquivo) (ok!)
# pegar informações do arquivo: tema, data, jornal, jornal-sigla, título, nome arquivo pdf (ok!)
# inserir metadados no xmp (ok!)
# Renomear dir_arquivo para dir_tif(PENDÊNCIA - Ctrl + H no Banco Json)
# Verificar inserção da data (exif-tool)
# inserir arquivos no Recool-web da hemeroteca

def consultar_json():
    ''' Responsável por encontrar o caminho do pdf a partir da base json'''
    dir_db = "/home/lantri_thiagofernandes/codigo/hemeroteca-peb/json/METADADOS_FINAL_ocr.json"
    db = TinyDB(dir_db,indent = 4, ensure_ascii=False)
    buscar = Query()
    for index,info in enumerate(iter(db),start=1):
        print(index)
        tema = info["tema"]
        data = info["data"]
        jornal = info["jornal"]
        jornal_sigla = info["jornal_sigla"]
        titulo_noticia = info["titulo_noticia"]
        nome_arq_pdf = info["nome_arquivo_pdf"]
        dir_pdf = info["dir_pdf"]
        dir_completo = dir_pdf + "/" + nome_arq_pdf
        #inserir_xmp(tema, data, jornal, jornal_sigla, titulo_noticia, nome_arq_pdf, dir_completo)
        inserir_metadados(tema, data, jornal, titulo_noticia, dir_completo)

def inserir_xmp(tema, data, jornal, jornal_sigla, titulo_noticia, nome_arq_pdf, dir_completo):
    pdf = Pdf.open(dir_completo, allow_overwriting_input = True)
    with pdf.open_metadata() as meta:
        meta["dc:tema"] = tema
        meta["dc:data"] = data
        meta["dc:jornal"] = jornal
        meta["dc:jornal_sigla"] = jornal_sigla
        meta["dc:titulo_noticia"] = titulo_noticia
        meta["dc:nome_arquivo_pdf"] = nome_arq_pdf
    pdf.save(dir_completo)
    meta = pdf.open_metadata()
    print(meta)

def inserir_metadados(tema, data, jornal, titulo_noticia, dir_completo):
    reader = PdfReader(dir_completo)
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Add the metadata
    writer.add_metadata(
        {
            "/Author": jornal,
            "/Title": titulo_noticia,
            "/Creator": data,
            "/Subject": tema,
            "/Keywords": tema
        }
    )

    # Save the new PDF to a file
    with open(dir_completo, "wb") as f:
        writer.write(f)


def main():
    consultar_json()

if __name__=='__main__':
    main()