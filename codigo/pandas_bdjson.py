#import io
#from google.colab import files
import pandas as pd
import json 
from pandas import json_normalize

def visualiza_dados ():
    #arq_json = files.upload()
    #df = pd.read_json(io.BytesIO(arq_json['teste.json']))
    df = pd.read_json('teste.json')
    print(df)
    with open('teste.json', 'r') as arq:
        dado = json.loads(arq.read())
    df_b = json_normalize(dado['_default'])
    print(df_b)

def main():
    visualiza_dados()

if __name__ == '__main__':
    main()