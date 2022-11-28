def cuadrados(lista):
   '''
   La funcion devuelve una lista de numeros elevados al cuadrado
   Parametros:
       - lista: una lista de numeros introducidos por el usuario
   Salidos:
       - lista de cuadrados: la lista de numeros elevada al cuadrado
   '''
   lista_cuadrados = []
   for n in lista:
       cuadrado = n**2
       lista_cuadrados.append(cuadrado)
   return lista_cuadrados
lista = []
while True:
   numero = int(input("Introduce un numero: "))
   if numero == 00:
       break
   lista.append(numero)
print(cuadrados(lista))
help(cuadrados)