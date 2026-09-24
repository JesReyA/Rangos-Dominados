#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:11:26 2026

@author: j
"""
import random as rn

def ordenar_puntos(lista):

    if(len(lista) <= 1):
        return lista
    else:
        indice_pivote = rn.randint(0, len(lista)-1)
        pivote = lista[indice_pivote]
        sobrante = lista[:indice_pivote] + lista[indice_pivote+1:]
        menores_pivote = [i for i in sobrante if i.coordenadax <= pivote.coordenadax]
        mayores_pivote = [i for i in sobrante if i.coordenadax > pivote.coordenadax]
        return ordenar_puntos(menores_pivote) + [pivote] + ordenar_puntos(mayores_pivote)
    

def crear_arbol_avl(lista):
    print("Aquí empieza el arbol, obvio esto se va a quitar")