import numpy as np
from colorama import Fore, Back, Style, init
init(autoreset=True)
def draw_player():
    matri = [[0,0,0,1,1,1,1,1,0,0,0,0],
             [0,0,0,1,1,1,1,1,0,0,0,0],
             [0,0,2,2,2,3,3,2,3,0,0,0],
             [0,2,3,2,3,3,3,2,3,3,3,0],
             [0,2,3,2,2,3,3,3,2,3,3,3],
             [0,2,2,3,3,3,3,2,2,2,2,0],
             [0,0,0,3,3,3,3,3,3,3,0,0],
             [0,0,1,1,4,1,1,4,1,1,0,0],
             [0,1,1,1,4,1,1,4,1,1,1,0],
             [1,1,1,1,4,4,4,4,1,1,1,1],
             [3,3,1,4,5,4,4,5,1,1,3,3],
             [3,3,3,4,4,4,4,4,4,3,3,3],
             [3,3,4,4,4,4,4,4,4,4,3,3],
             [0,0,4,4,4,0,0,4,4,4,0,0],
             [0,0,2,2,0,0,0,0,2,2,0,0],
             [0,2,2,2,0,0,0,0,2,2,2,0]]

    matriz_np = np.array(matri)
    matriz_np[0,3:8]=1
    matriz_np[1,2:11]=1
    matriz_np[2,2:5]=2
    matriz_np[2,5:7]=3
    matriz_np[2,7]=2
    matriz_np[2,8]=3 #fila 3
    matriz_np[3:6,1]=2
    matriz_np[3:5,2]=3
    matriz_np[3:5,3]=2
    matriz_np[3,4:7]=3
    matriz_np[3,7]=2
    matriz_np[3,8:11]=3
    matriz_np[4,9:12]=3
    matriz_np[4,8]=2
    matriz_np[4,5:8]=3
    matriz_np[4,4]=2
    matriz_np[5,2]=2
    matriz_np[5,3:7]=3
    matriz_np[5,7:11]=2
    matriz_np[6,2:10]=3

    for i in matriz_np:
        for j in i:
            if j==0:
                print(Back.WHITE + "   ",end="")
            elif j == 1:
                print(Back.LIGHTRED_EX + "   ", end="")
            elif j == 2:
                print(Back.BLACK + "   ", end="")
            elif j == 3:
                print(Back.LIGHTWHITE_EX + "   ", end="")
            elif j == 4:
                print(Back.LIGHTBLUE_EX + "   ", end="")
            elif j == 5:
                print(Back.LIGHTYELLOW_EX + "   ", end="")
        print(" ")
draw_player()



