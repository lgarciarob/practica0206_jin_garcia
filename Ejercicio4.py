def media(lista):
    '''
    La funcion devuelve la media de una lista de numeros
    Parametros:
        - lista: lista de numeros introducidos por el usuario
    Salidas:
        - media: la media aritmetica de la lista de numeros
    '''
    media = sum(lista) / len(lista)
    return media


lista = []
while True:
    numero = int(input("Introduce un numero: "))
    if numero == 00:
        break
    lista.append(numero)
print(media(lista))
help(media)