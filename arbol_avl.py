#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 00:21:30 2026

@author: j
"""
from nodo_arbol import Nodo

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        
    def obtener_altura(self, nodo):
        return 0 if(nodo) == None else nodo.altura
    
    def factor_balance(self, nodo):
        return 0  if (nodo) == None else self.obtener_altura(nodo.hijo_izquierdo) - self.obtener_altura(nodo.hijo_derecho)