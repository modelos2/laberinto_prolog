import numpy as np
import os
# from pyswip import Prolog
import tkinter as tk
from tkinter import Canvas

f = open('labe.pl', 'w')
f.write('')

archivo = ''


def leer():
    return [x.split(' ') for x in open('laberinto.txt', 'r')]


def arreglada():
    # .replace('\n','')
    # se genera la matriz ya en forma matricial quedando para manejar de la siguiente manera matriz[i][j]
    return [[x.replace('\n', '') for x in y] for y in leer()]


print(np.array(arreglada()))
print(len(arreglada()))
l = []
for lista in range(len(arreglada())):
    for i in range(len(arreglada()[lista])):
        if lista == 0 and arreglada()[lista][i] == 'I':
            l.append('conecta(' + arreglada()[lista][i] + ',' + arreglada()[lista + 1][i] + ')')
            archivo = 'conecta(inicio' + ',' + arreglada()[lista + 1][i] + ').'

        if lista > 0 and arreglada()[lista][i] != '|' and arreglada()[lista][i] != '-' and arreglada()[lista][i] != '0':
            # en esta parte  ya esta ubicado en los numeros y letras "por el I de inicio y F de fin"
            # en los que toca hacer la evaluacion
            if i < 12 and arreglada()[lista][i + 1] == '0' and int(arreglada()[lista][i + 2]) > 0:
                l.append('conecta(' + arreglada()[lista][i] + ',' + arreglada()[lista][i + 2] + ')')
                archivo = archivo + '\n' + 'conecta(' + arreglada()[lista][i] + ',' + arreglada()[lista][i + 2] + ').'
            if lista < 12 and arreglada()[lista + 1][i] == '0' and int(arreglada()[lista + 2][i]) > 0:
                l.append('conecta(' + arreglada()[lista][i] + ',' + arreglada()[lista + 2][i] + ')')
                archivo = archivo + '\n' + 'conecta(' + arreglada()[lista][i] + ',' + arreglada()[lista + 2][i] + ').'
            if lista == 12 and arreglada()[lista + 2][i] == 'F':
                l.append('conecta(' + arreglada()[lista][i] + ',' + arreglada()[lista + 2][i] + ')')
                archivo = archivo + '\n' + 'conecta(' + arreglada()[lista][i] + ',' + 'fin).'

print(l)

archivo = archivo + '\n' + 'conectado(Pos1,Pos2) :- conecta(Pos1,Pos2).'
archivo = archivo + '\n' + 'conectado(Pos1,Pos2) :- conecta(Pos2,Pos1).'
archivo = archivo + '\n' + 'miembro(X,[X|_]).'
archivo = archivo + '\n' + 'miembro(X,[_|Y]) :- miembro(X,Y) .'
archivo = archivo + '\n' + 'sol :- camino([inicio],Sol),write(Sol) .'
archivo = archivo + '\n' + 'camino([fin|RestoDelCamino],[fin|RestoDelCamino]).'
archivo = archivo + '\n' + 'camino([PosActual|RestoDelCamino],Sol) :- conectado(PosActual,PosSiguiente),\+ miembro(PosSiguiente,RestoDelCamino),camino([PosSiguiente,PosActual|RestoDelCamino],Sol).'
f.write(archivo)
f.close()

# prolog = Prolog()
# prolog.consult('labe.pl')
# solucion = prolog.query("sol")
solucion = ['fin', 32, 33, 34, 28, 27, 26, 20, 14, 15, 21, 22, 16, 10, 4, 3, 2, 'inicio']
solucion.reverse()
print(solucion)


def dibujar():
    lienzo = Canvas(marco, width=500, height=500, background="white")
    lienzo.grid(row=6, column=0)
    x = 30
    y = 20
    for lista in range(len(arreglada())):
        for i in range(len(arreglada()[lista])):
            if lista % 2 == 0 and i % 2 != 0 and lista > 0 and lista < 14:
                print(int(arreglada()[lista][i]))
                if int(arreglada()[lista][i]) in solucion:
                    lienzo.create_text(x, y, text=arreglada()[lista][i], fill='red')
                else:
                    lienzo.create_text(x, y, text=arreglada()[lista][i])
                if arreglada()[lista - 1][i] == '-':
                    lienzo.create_line(x - 20, y - 20, x + 20, y - 20)
                if arreglada()[lista + 1][i] == '-':
                    lienzo.create_line(x - 20, y + 20, x + 20, y + 20)
                if arreglada()[lista][i - 1] == '|':
                    lienzo.create_line(x - 20, y - 20, x - 20, y + 20)
                if arreglada()[lista][i + 1] == '|':
                    lienzo.create_line(x + 20, y - 20, x + 20, y + 20)
                x = x + 40
        x = 30
        y = y + 20


# Abre el marco
marco = tk.Tk()
marco.title("Laberinto")
marco.geometry("500x500")
dibujar()
marco.mainloop()
