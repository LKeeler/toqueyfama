#!/usr/bin/python3
# -*- coding: utf-8 -*-

VERSION ="3.0-r2"

import random
import string

numero=["0","1","2","3","4","5","6","7","8","9"]
d_turnos={"baja":100, "media":40, "alta":15}

clave= random.choice(numero)
numero.remove(clave)

for i in range(3):
    c = random.choice(numero)
    numero.remove(c)
    clave= clave+c

print("Toque y Fama".center(78))
for i in range(22):
    print()
print("Ingrese enter para continuar".rjust(78))
input()

dificultad= random.choice(["baja","media", "alta"])
turnos= d_turnos[dificultad]
print("Le tocó dificultad: ", dificultad)

for it in range(turnos):
    cToque=0
    cFama=0
    num = str(input("Le quedan "+str(turnos-it)+", ingrese un número de 4 dígitos: "))
    if len(num)== 4:
        for i in num:
            if i in clave:
                cToque+=1
        for i in range(4):
            if num[i] == clave[i]:
                cFama+=1

        if cFama < 4:
            print("Número de toques", cToque-cFama ,"y número de famas", cFama)
            print()
        else:
            print("Congratulaciones usted ganó")
            break
    else:
        print("Ingreso incorrecto, trate de nuevo")
        print
