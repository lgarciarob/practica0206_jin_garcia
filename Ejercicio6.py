def dec_bin(decimal):
    """"
     Esta funcion convierte el numero decimal dado por el usuario en su equivalente binario

     Parametros:
         - decimal: es el numero que introduce el usuario para que la funcion lo convierta a binario
     Salidas:
         - binario: es el numero que ha introducido el usuario, convertido en binario
     """

    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return binario


def bin_dec(binario):
    """"
    Esta funcion convierte el numero binario introducido a su equivalente en decimal

    Parametros:
        -binario= es el numero que introduce el usuario para ser convertido a binario
    Salidas:
        -decimal= es el numero binario introducido ya convertido a decimal
    """

    numero_decimal = 0
    for posicion, digito in enumerate(numero_binario[::-1]):
        numero_decimal += int(digito) * 2 ** posicion

    return numero_decimal


print(dec_bin(int(input("Introduzca el numero(en decimal) que quieres convertir a binario: "))))
print(bin_dec(input("Introduzca el numero (en binario) que quieres convertir a decimal: ")))