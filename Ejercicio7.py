def creador_dict(cadena):
  '''
  Una funcion que recibe una cadena de caracteres y regresa un diccionario con cada palabra que contiene y su frecuencia.
  Parametros:
        - cadena: palabras dadas por el usuario
  Salida:
        - diccionario: devuelve la palabra mas frecuente en el diccionario y su frecuencia
  '''

  lista_1 = cadena.split()
  dict_1 = {}
  for i in list_1:
    if i in dict_1:
      dict_1[i] +=1
    else:
      dict_1[i] = 1
  return dict_1

def contador_dict(dictionario):
  '''
  Una funcion que recibe un diccionario y regresa una tupla: la palabra mas repetida y cuantas veces aparece
  Parametros:
        - diccionario: las palabras que ingresa el usuario
  Salidas:
        - tupla: devuelve la palabra mas repetida y cuantas veces aparece
  '''
  palabra_frecuente = ''
  cantidad = 0
  for keys , values in dictionario.items():
    if values > cantidad:
      cantidad = values
      palabra_frecuente = keys
  return palabra_frecuente , cantidad

entrada = input('Ingrese su cadena de caracteres: ')
print(creador_dict(entrada))
print(contador_dict(entrada))
help(creador_dict)
help(contador_dict)