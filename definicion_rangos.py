#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:00:37 2026

@author: erikazr
"""
import logica_puntos
from punto_coordenadas import PuntoCoordernadas

punto_mayor = ""
punto_A = PuntoCoordernadas("A", 3, 4)
punto_B = PuntoCoordernadas("B", 8, 2)
punto_C = PuntoCoordernadas("C", 1, 6)
punto_D = PuntoCoordernadas("D", 0, 7)
punto_E = PuntoCoordernadas("E", 5, 1)

lista_puntos=[]
lista_puntos.append(punto_A)
lista_puntos.append(punto_B)
lista_puntos.append(punto_C)
lista_puntos.append(punto_D)
lista_puntos.append(punto_E)

print(lista_puntos)

lista_ordenada = logica_puntos.ordenar_puntos(lista_puntos)

print(lista_ordenada)