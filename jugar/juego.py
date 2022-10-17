from comparacion import *
from main import usuario
from niveles import*


print("Introduzca el número a adivinar")
while True:
    # Entramos en un bucle infinito

    # Pedimos introducir un número
    numero = input("Introduzca un número entre 0 y 99 incluídos: ")

    try:
        numero = int(numero)
    except:
        pass
    else:
        # Hacer la comparación
        if 0 <= numero <= 99:
            # Tenemos lo que queremos, salimos del bucle
            break

# PARTE 2
def usuario (numero):
    print("intente encontrar el número a adivinar")
    while True: 
        while True: 
            intento = input("Introduzca un número entre 0 y 99 incluídos: ")
            try:
             intento = int(intento)
            except:
                pass
            else:
            # Hacer la comparación
                 if 0 <= intento <= 99:
                # Tenemos lo que queremos, salimos del BUCLE 2
                    break

    # Se prueba si el intento es correcto o no
            if intento < numero:
                print("Demasiado pequeño")
            elif intento > numero:
                print("Demasiado grande")
            else:
                print("Victoria!")
        # Terminamos la partida, salimos del BUCLE 1
                break