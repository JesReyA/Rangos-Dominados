#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:00:37 2026

@author: erikazr
"""

from PuntoCoordenadas import PuntoCoordernadas

punto_mayor = ""
punto_A = PuntoCoordernadas("A", 1, 2)
punto_B = PuntoCoordernadas("B", 2, 4)
punto_C = PuntoCoordernadas("C", 3, 3)
punto_D = PuntoCoordernadas("D", 4, 6)
punto_E = PuntoCoordernadas("E", 7, 1)

lista_puntos=[]
lista_puntos.append(punto_A)
lista_puntos.append(punto_B)
lista_puntos.append(punto_C)
lista_puntos.append(punto_D)
lista_puntos.append(punto_E)

print(lista_puntos)