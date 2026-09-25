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
    
    
    def rotacion_izquierda(self, nodo):
        nuevo_nodo_raiz = nodo.hijo_derecho             #Variable para guardar el nodo que subirá
        
        nodo_intercambiable_guardado = nuevo_nodo_raiz.hijo_izquierdo  #Variable necesaria para guardar el nodo de forma temporal
    
        nuevo_nodo_raiz.hijo_izquierdo = nodo           #El hijo izquierdo del nodo raíz ahora es todo todo lo que esta a la izquierda del raiz anterior, incluido este
        
        nodo.hijo_derecho = nodo_intercambiable_guardado        #El hijo derecho del subarbol izquierdo es el nodo que se guardó para no perderse
        
        #Se calculan las alturas de los subarboles modificados y se suma uno por el nodo actual que se toma en cuenta
        nodo.altura = 1 + max(self.obtener_altura(nodo.hijo_izquierdo),self.obtener_altura(nodo.hijo_derecho))
        nuevo_nodo_raiz.altura = 1 + max(self.obtener_altura(nuevo_nodo_raiz.hijo_izquierdo),self.obtener_altura(nuevo_nodo_raiz.hijo_derecho))
        
        #Se retorna el nodo que se ha modificado o subido para ser el nuevo
        return nuevo_nodo_raiz
    
    def rotacion_derecha(self, nodo):
        nuevo_nodo_raiz = nodo.hijo_izquierdo            #Variable para guardar el nodo que subirá
        
        nodo_intercambiable_guardado = nuevo_nodo_raiz.hijo_derecho  #Variable necesaria para guardar el nodo de forma temporal
    
        nuevo_nodo_raiz.hijo_derecho = nodo           #El hijo derecho del nodo raíz ahora es todo todo lo que esta a la derecha del raiz anterior, incluido este
        
        nodo.hijo_izquierdo = nodo_intercambiable_guardado        #El hijo izquierdo del subarbol derecho es el nodo que se guardó para no perderse
        
        #Se calculan las alturas de los subarboles modificados y se suma uno por el nodo actual que se toma en cuenta
        nodo.altura = 1 + max(self.obtener_altura(nodo.hijo_izquierdo),self.obtener_altura(nodo.hijo_derecho))
        nuevo_nodo_raiz.altura = 1 + max(self.obtener_altura(nuevo_nodo_raiz.hijo_izquierdo),self.obtener_altura(nuevo_nodo_raiz.hijo_derecho))
        
        #Se retorna el nodo que se ha modificado o subido para ser el nuevo
        return nuevo_nodo_raiz
        