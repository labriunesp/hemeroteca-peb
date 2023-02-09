from tinydb import TinyDB,Query
from unidecode import unidecode

def nomes_jornais():
    bd = TinyDB('/media/hdvm08/bd/002/997/001/json/metadados_bons2.json')
    busca = Query()
    for index, noticia in enumerate(bd, start=1):
        if noticia['jornal_sigla'] == 'JB':
            noticia['jornal'] = 'Jornal do Brasil'
            #print(noticia['jornal'])
        elif noticia['jornal_sigla'].lower() == 'valor':
            atualiza = bd.update({'jornal_sigla':'valor'|'Valor'|'VALOR'},busca.jornal_sigla=="VLR")
            bd.update({'jornal_sigla':'VLR'},busca.jornal=='Valor Econômico')
            print(atualiza)
        elif noticia['jornal_sigla'] == 'JT':
            noticia['jornal'] = 'Jornal da Tarde'
            #print(noticia['jornal'])
        elif noticia['jornal_sigla'].lower() == 'veja':
            noticia['jornal'] = 'Veja'
            noticia['jornal_sigla'] = 'Veja'
            #print(noticia['jornal'])
        elif unidecode(noticia['jornal_sigla'].lower()) == 'clarin':
            noticia['jornal'] = 'Clarín'
            noticia['jornal_sigla'] = 'Clarin'
            #print(noticia['jornal'])
        elif noticia['jornal_sigla'] == 'OESP':
            noticia['jornal'] = 'O Estado de S. Paulo'
            noticia['jornal_sigla'] = 'ESP'
            #print(noticia['jornal'])
        elif noticia['jornal_sigla'].lower() == 'estadao':
            noticia['jornal'] = 'O Estado de S. Paulo'
            noticia['jornal_sigla'] = 'ESP'
            #print(noticia['jornal'])
        elif noticia['jornal_sigla'] == 'JC':
            noticia['jornal'] = 'Jornal do Comércio'
            #print(noticia['jornal'])
        elif unidecode(noticia['jornal_sigla'].lower()) == 'istoé':
            noticia['jornal'] = 'IstoÉ'
            noticia['jornal_sigla'] = 'IstoE'
            #print(noticia['jornal'])
        elif noticia['jornal_sigla'] == 'SBPC':
            noticia['jornal'] = 'Sociedade Brasileira para o Progresso da Ciência'
            #print(noticia['jornal'])
        elif noticia['jornal_sigla'].lower() == 'dailypost':
            noticia['jornal'] = 'Dailypost'
            noticia['jornal_sigla'] = 'DAILYPOST'
            #print(noticia['jornal'])
        
        
def main():
    nomes_jornais()
    

if __name__ == '__main__':
    main()