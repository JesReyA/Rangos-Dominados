#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:59:25 2026

@author: j
"""

class Nodo:
    def __init__(self, coordenada_y_punto, punto_referenciado, altura = 1, hijo_izquierdo= None, hijo_derecho = None):
        self.hijo_izquierdo = hijo_izquierdo                   #Puntero al hijo del nodo
        self.hijo_derecho = hijo_derecho                       #Puntero al hijo del nodo
        
        self.coordenada_y_punto = coordenada_y_punto           #Coordenada guardada de cada punto que se compara
        self.punto_referenciado = punto_referenciado          #Referencia al punto completo del cual pertenece la coordenada, servirá para mencionar exactamente a cuales se domina
        self.altura = altura                                  #Se usará al momento del balanceo del arbol, además de en la parte de sweep line
        