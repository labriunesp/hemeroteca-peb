from pikepdf import Pdf
from tinydb import TinyDB,Query 
from PyPDF2 import PdfReader, PdfWriter
from typing_extensions import TypeAlias
from datetime import datetime
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

# consultar a base json (pegar o caminho do arquivo) (ok!)
# pegar informações do arquivo: tema, data, jornal, jornal-sigla, título, nome arquivo pdf (ok!)
# inserir metadados no xmp (ok!)
# Renomear dir_arquivo para dir_tif(PENDÊNCIA - Ctrl + H no Banco Json)
# Verificar inserção da data (exif-tool)
# Pôr o CreationDate em todos os arquivos no seguinte formato: 'D:20220928181800-0300'
# inserir arquivos no Recoll-web da hemeroteca
# https://github.com/unitedstates/inspectors-general/issues/31
# https://stackoverflow.com/questions/68019092/pdf-getdocumentinfo-date-format
# https://nanonets.com/blog/pypdf2-library-working-with-pdf-files-in-python/

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
            "/Keywords": tema,
            "/CreationDate": "D:20220928181800-0300"
        }
    )

    # Save the new PDF to a file
    with open(dir_completo, "wb") as f:
        writer.write(f)

def inserir_data():
    data_criacao = "D:20220928181800-0300"
    data = datetime.strptime(data_criacao, "D:%Y%m%d%H%M%S%z")
    print(data)

def pdfminer():
    fp = open('/media/hdvm08/bd/002/997/001/pdf/03-brasil-argentina/0000-00-00-GZM-Produtores_acreditam_na_manuntencao_de_sobretaxa-p01.pdf', 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)

    print(doc.info)  # The "Info" metadata

def main():
    #consultar_json()
    #inserir_data()
    pdfminer()

if __name__=='__main__':
    main()