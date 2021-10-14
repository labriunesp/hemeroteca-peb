def inserir_metadados():
    nome = 'ana'
    print (nome)


def numeros():
    numero_01 = int(input('Insira um número: '))
    numero_02 = int(input('Insira outro número: '))
    return numero_01 , numero_02

def somar():
    numeros_todos = numeros()
    print (numeros_todos)
    somar = numeros_todos [0] + numeros_todos [1]
    print (f'A soma de {numeros_todos [0]} com {numeros_todos [1]} é: {somar}')
    return somar


def subtrair():
    soma = somar()
    print (soma)
    numero = int(input (f'Indique o número para subtrair de {soma}: '))
    subtraçao = soma - numero
    print (f'O resultado da subtração é: {subtraçao}')
    #return print (subtraçao)
    
def multiplicar():
    pass

def dividir():
    pass

def main ():
    #metadados = inserir_metadados()
    somar_numeros = somar()
    subtrair_numero = subtrair()

if __name__ == "__main__": 
    main ()
