def normalizar_sigla():
    teste = "2010-12-29-ESP_WikiLeaks_põe_Brasil_na_rota_da_droga.tif"
    normalizar = teste.replace("_", "-")
    lista = normalizar.split("-")
    print(lista)
    lista = lista[4:]
    print(lista)
    lista = " ".join(lista)
    print(lista)

def main():
    normalizar_sigla()
    

if __name__ == '__main__':
    main()