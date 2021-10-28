import os # biblioteca nativa (vem junto com o python)
import sh # biblioteca de terceiro

def listar_arquivos():
    """responsável por lista os arquivos da pasta
    lista em python >>> ['estrutura-basica.py', 'intro_02.py', 'intro_01.py', 'teste02', 'teste01']
    tupla em python >> ('/home/lantri_rafael/codigo/hemeroteca-peb/intro-python/rafael', 'intro_02.py')
    """
    lista_arquivos = os.listdir() # lista em python (iteravel)
    lista_geral = [] # lista vazia

    # Controle de fluxo, estrutura de repetição, lopp for
    for elemento in lista_arquivos:
        lista_geral.append(elemento[-1])
    
    return lista_geral
        

def nome_diretorio():
    nome_dir = os.path.dirname("/home/lantri_rafael/codigo/hemeroteca-peb/intro-python/rafael/intro_02.py")
    nome_arquivo = os.path.basename("/home/lantri_rafael/codigo/hemeroteca-peb/intro-python/rafael/intro_02.py")
    nome_dir_e_arquivo = os.path.split("/home/lantri_rafael/codigo/hemeroteca-peb/intro-python/rafael/intro_02.py") # retorna uma tupla
    print(nome_dir) 
    print(nome_arquivo) 
    print(nome_dir_e_arquivo)
    print(nome_dir_e_arquivo.index('/home/lantri_rafael/codigo/hemeroteca-peb/intro-python/rafael')) 
    
    for el in nome_dir_e_arquivo:
        print(el)
    



def criar_diretorio():
    """responsável por criar diretorios"""
    cria_diretorio = os.makedirs("teste02", exist_ok = True)
    print("Diretorio criado - intro_02")





def main():
    nome_diretorio()
    listar_arquivos()
    #criar_diretorio()

if __name__ == "__main__":
    main()

