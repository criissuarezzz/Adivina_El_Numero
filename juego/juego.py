
import sys
from main.main import usuario
from niveles.niveles import*


def pedir_numero(): 
    while True: 
        entrada = input("Introduce un número") 
        try: 
            entrada = int(entrada) 
        except: 
            print("Solo están autorizados los caracteres [0-9].", file=sys.stderr) 
        else: 
            break
    return entrada 


# PARTE 2

from niveles.niveles import niveles(elige_nivel)

def pedir_numero_limite(minimo=MIN, maximo=MAX): 
    while True: 
        invitacion = "Elige un número entre {} y {} incluidos".format(minimo, maximo) 
        entrada = pedir_numero(invitacion) 
        if minimo <= entrada <= maximo:
            return entrada 

def usuario (numero):
    print("intente encontrar el número a adivinar")
    while True:  
         intento=pedir_numero()
            # Hacer la comparación
         if 0 <= intento <= 99:
        # Tenemos lo que queremos, salimos del BUCLE 
        # Se prueba si el intento es correcto o no
            if intento < numero:
                print("Demasiado pequeño")
            elif intento > numero:
                print("Demasiado grande")
            else:
                print("Victoria!")
        # Terminamos la partida, salimos del BUCLE 1
                break


def jugar_una_vez(numero, minimo, maximo): 
    intento=0
    intento = pedir_numero_limite("Adivine el número", minimo, maximo) 
    if intento < numero: 
        print("Demasiado pequeño") 
        minimo = intento + 1 
        victoria = False 
    elif intento > numero: 
        print("Demasiado grande") 
        maximo = intento - 1 
        victoria = False 
    else: 
        print("¡Ha ganado!") 
        victoria = True 
        minimo = maximo = intento 
    return victoria, minimo, maximo 
print(intento)

def jugar_una_partida(numero, minimo, maximo): 
   while True: 
    victoria, minimo, maximo = jugar_una_vez(numero, minimo, maximo,)  
    if victoria: 
        break
nombre= input("Introduce tu nombre")
puntuacion= []
def guardar_puntuacion(nombre_archivo, puntuacion):
    
    archivo = open(nombre_archivo, "w")
    for nombre, intento in jugar_una_vez:
        archivo.write(nombre+","+str(intento)+"\\n")
    archivo.close()



