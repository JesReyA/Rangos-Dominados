#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 01:30:46 2026

"""

class PuntoCoordernadas:
    def __init__(self, coordenadax, coordenaday):
        self.coordenadax = coordenadax
        self.coordenaday = coordenaday
    
    def __repr__(self):
        return f"{self.coordenadax}, {self.coordenaday}"