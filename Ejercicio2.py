def factorial_bucle(numero):
   '''
       Esta funcion calcula el factorial de un numero entero introducido por el usuario
   Parametros:
       -numero: numero introducido por el usuario
   Salidas:
       -factorial: devuelve el factorial del numero
   '''
   factorial = 1
   for n in range(1, numero+1):
       factorial = factorial * n
   return factorial
numero = int(input("Introduce un numero:\n"))
print(factorial_bucle(numero))
help(factorial_bucle)

def factorial_recursivo(numero):
   '''
   Esta funcion calcula el factorial de un numero entero introducido por el usuario
   Parametros:
       - numero: un numero introducido por el usuario
   Salidas:
       - fact: devuelve el factorial del numero
   '''
   if numero == 0:
       return 1
   else:
       fact = numero * factorial_recursivo(numero-1)
       return fact
numero = int(input("Introduce un numero:\n"))
print(factorial_recursivo(numero))
help(factorial_recursivo)