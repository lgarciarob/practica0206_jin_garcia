def area(radio):
    '''
   La funcion calcula el area de un circulo con un radio dado
   Parametros:
       - radio: un numero introducido por el usuario que representa el radio del circulo
   Salidas:
       -area: devuelve el area calculada
   '''
    area = 3.14 * radio ** 2
    return area


def volumen(altura):
    '''
   La funcion devuleve el volumen del cilindro con una altura dada
   Parametros:
       - altura: un numero introducido por el usuario que representa el volumen del cilindro
   Salidas:
       - volumen: devuelve el volumen calculado
   '''
    area_circulo = area(radio)
    volumen = area_circulo * altura
    return volumen

radio = float(input("Introduce el radio del circulo"))
print(area(radio))
help(area)
altura = float(input("Introduce la altura del cilindro"))
print(volumen(altura))
help(volumen)