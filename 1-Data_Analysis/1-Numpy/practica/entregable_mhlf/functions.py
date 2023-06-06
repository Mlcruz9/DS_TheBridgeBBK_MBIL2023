import numpy as np
from variables import tablero, lista_barcos


def colocar_barco():
   
    for i in lista_barcos:
        for j in i:
            tablero[j] = "O"
    
    print(tablero)

def disparar():
    coor_x = int(input("Introduzca la coordenada X de su disparo: "))
    coor_y = int(input("Introduzca la coordenada Y de su disparo: "))

    if tablero[coor_x, coor_y] == "O":
        tablero[coor_x, coor_y] = "X"
        print("Has acertado, juega nuevamente!")
        print(tablero)
    
    elif tablero[coor_x, coor_y] == " ":
        tablero[coor_x, coor_y] = "-"
        print("Has fallado!")
        print(tablero)
    
    elif tablero[coor_x, coor_y] == "X":
        print("Has hecho este disparo anteriormente, intenta de nuevo")
        print(tablero)

    elif tablero[coor_x, coor_y] == "-":
        print("Has hecho este disparo anteriormente, intenta de nuevo")
        print(tablero)
    

def barco_aleatorio(eslora):
    orientaciones = ["N", "S", "E", "O"]

    np.random.seed(0)
    coor_x = np.random.randint(10)
    coor_y = np.random.randint(10)
    np.random.seed(6)

    orien = np.random.choice(orientaciones)
    print(orien)
    print(coor_x)

    if orien == "E":
        tablero[coor_x, coor_y:coor_y + eslora] = "O"
    
    print(tablero)
