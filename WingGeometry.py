# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 07:42:50 2021

@author: marco
"""
#Bibliotecasimport numpy as np
import math
import os

#Criador de pastas
def check(): 
  path = 'analyse project'
  if not os.path.exists(path):
     os.makedirs('analyse project')  

#Classe da asa
class wing:
    def __init__(self, cr, ct, b_ret):
        self.cr = cr  #Intervalos da Corda na raiz
        self.ct = ct #Intervalos da Corda na ponta
        self.b_ret = b_ret #Intervalos da Envergadura da asa
        self.af = list()    #Declaração da relação de afilamento como lista
        
        for i in range(0, len(self.cr)):
            self.af.append(self.ct[i]/self.cr[i])
        for i in range(0, len(self.af)):
            if(self.af[i] >= 0.5 and self.af[i] <=0.52):
                self.af = self.af[i]
                self.cr = self.cr[i]
                self.ct = self.ct[i]
                self.b_ret = self.b_ret[i]
                break
        self.b_tra = 2.0 - self.b_ret
        self.b = self.b_ret + self.b_tra
        self.S_ret = self.b_ret * self.cr
        self.S_tra = ((self.cr+self.ct)*self.b_tra)/2
        self.S = self.S_ret + self.S_tra
        self.AR = math.pow(self.b, 2)/self.S
        self.c =  (2/3) * self.cr * ((1+self.af+math.pow(self.af, 2))/(1+self.af))
        self.e = 1.78*(1-(0.045*math.pow(self.AR,0.68)))-0.64
        
    def results(self):
        data = open('analyse project/wing geometry.txt', 'w')
        line = list()
        line.append('-----------------------------------------------\n')
        line.append('\tParâmetros Geométricos da Asa\n')
        line.append('-----------------------------------------------\n')
        line.append('Corda na raiz(cr): {}m\n'.format(self.cr))
        line.append('Corda na ponta(ct): {}m\n'.format(self.ct))
        line.append('Envergadura retangular(b_ret): {}m\n'.format(self.b_ret))
        line.append('Envergadura trapezoidal(b_tra): {}m\n'.format(self.b_tra))
        line.append('Envergadura(b): {}m\n'.format(self.b))
        line.append('Área da asa retangular(S_ret): {}m²\n'.format(self.S_ret))
        line.append('Área da asa retangular(S_tra): {}m²\n'.format(self.S_tra))
        line.append('Área da asa: {}m²\n'.format(self.S))
        line.append('Corda média aerodinâmica: {}m\n'.format(self.c))
        line.append('Alongamento: {}\n'.format(self.AR))
        line.append('Afilamento: {}\n'.format(self.af))
        line.append('-----------------------------------------------\n')
        data.writelines(line)
        data.close()

