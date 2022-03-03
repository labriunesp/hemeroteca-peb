#import io
#from google.colab import files
import chardet
import pandas as pd
import json 
from pandas import json_normalize

# https://archive.is/Jt493
# https://archive.is/ESefi
# https://archive.is/pFvWS
# https://www.kaggle.com/rtatman/automatically-detecting-character-encodings
# https://towardsdatascience.com/a-guide-to-unicode-utf-8-and-strings-in-python-757a232db95c

def visualiza_dados ():
    df = pd.read_json('teste.json', orient='columns')
    df = pd.json_normalize(df['_default'])
    #print(df)
    '''print(df.shape)
    print(df.columns)
    print(df.head())
    print(df.tail())
    print(df.dtypes)
    print(df.describe())'''
    #print(df['quant_pages'].sum())
    #print(df['data'])
    #data_ruim = df.query('data == "00/00/0000"')
    data_ruim = df.loc[~df['data'].str.contains('[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]')]
    print(data_ruim)
    sigla_ruim = df.loc[~df['jornal_sigla'].str.contains('ESP|FSP|GM|GZM', na=False)]
    print(sigla_ruim['jornal_sigla'])
    titulo_ruim = df.loc[df['titulo_noticia'].str.contains('NA')]
    print(titulo_ruim['titulo_noticia'])

def ajustar_nome():
    arquivos = ['2002-03-26GM-UE_sobretaxa_ao_aÃ§o_entre_14-9_a_26%' , '2002-03-26GM-UE_sobretaxa' ]
    for arquivo in arquivos:
    arquivo = arquivo
    print(arquivo)
    try:
        descobrir = chardet.detect(arquivo.encode("ascii"))
        print(descobrir)
    except UnicodeEncodeError as e:
        print(e)
        arquivo = arquivo.encode('iso-8859-1').decode('utf-8')
        print(arquivo)
    

def main():
    #visualiza_dados()
    ajustar_nome()
if __name__ == '__main__':
    main()