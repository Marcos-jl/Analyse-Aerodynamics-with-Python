#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 12:19:51 2022

@author: marcos
"""
#Importando Bibliotecas
import WingGeometry
import WingAerodynamics
import numpy as np

#Chama o módulo de criar pasta
WingGeometry.check()

#Input
cr = np.linspace(0.25,0.50,num=20)
ct = np.linspace(0.1,0.3,num=20)
b_ret = np.linspace(1.10,1.30,num=20)

#Output
asa = WingGeometry.wing(cr, ct, b_ret)
asa.results()

#Análise Aerodinâmica
analise = WingAerodynamics.wing(asa.cr, asa.ct, asa.af, asa.c, asa.b_ret, asa.b_tra, asa.b, asa.S_ret, asa.S_tra, asa.S, asa.AR, asa.e)
analise.Lift()
analise.Drag()
analise.Efficiency()
analise.Moment()
