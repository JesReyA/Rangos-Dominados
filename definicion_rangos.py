#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:00:37 2026

@author: erikazr
"""

from PuntoCoordenadas import PuntoCoordernadas

puntoPrueba = PuntoCoordernadas("a", 1, 2)
puntoPrueba2 = PuntoCoordernadas("b", 2, 3)

listaPuntos =[]
listaPuntos.append(puntoPrueba)
listaPuntos.append(puntoPrueba2)

print(listaPuntos[0].etiqueta)