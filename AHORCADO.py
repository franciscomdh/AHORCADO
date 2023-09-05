# =============================================================================
# FRANCISCO DIAZ HERRERO
# =============================================================================
from pathlib import Path
import re
import random
# =============================================================================
# =============================================================================
# =============================================================================
#                              PROYECTO: AHORCADO
# =============================================================================
# =============================================================================
# =============================================================================

directorio=Path("/DIFICULTAD/")
print("\033[1;30;40m #############################################")
print("\033[0;33;47m                   AHORCADO!                  ")
print("\033[1;30;40m #############################################")
print("")
print("\033[10;37;40m                    MENU                      ")
print("")
print("\033[1;36;40m 1.JUGAR ")
print("\033[1;36;40m 3.SALIR ")
opc=input("\u001b[0m INGRESE LA OPCION\n")
    
if(opc=="1"):
    opc=0
    print("\033[1;36;40m           SELECCIONE LA DIFICULTAD           ")
    print("\033[1;36;40m 1.FACIL")
    print("\033[1;36;40m 2.MEDIO")
    print("\033[1;36;40m 3.DIFICIL")

    opc=input("\u001b[0m INGRESE LA OPCION\n")
    
    if(opc==1):
        miarc=open(directorio/"FACIL.txt","r",encoding="utf8")
        lista1=miarc.readlines()
        for i in range(len(lista1)):
            lista1[i]=lista1[i].rstrip("\n")
        palabra=lista1.choice()
        print(palabra)
    if(opc==2):
        miarc=open(directorio/"MEDIO.txt","r",encoding="utf8")
        lista2=miarc.readlines()
    if(opc==3):
        miarc=open(directorio/"DIFICIL.txt","r",encoding="utf8")
        lista3=miarc.readlines()
    
if(opc=="2"):
    print("HASTA PRONTO!")
