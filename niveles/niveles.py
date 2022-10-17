
elige_nivel: input("¿Qué nivel deseas jugar? 1 para primer nivel (de 0 a 99), 2 para segundo nivel (de 0 a 1000), 3 para tercer nivel(0 a 10000) ")

def niveles(elige_nivel):
    if "1" in elige_nivel:
        MIN=0
        MAX=99
    elif "2" in elige_nivel:
        MIN=0
        MAX=1000
    elif "3" in elige_nivel:
        MIN=0
        MAX=10000
