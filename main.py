from math import *


#Velocidade da luz no vacuo
c = 3E8

#Massa do eletron
me = 9.11E-31

#Constante magnetica
𝜇0 = (4*pi)*10**-7

#Constante de Planck em J x s
hJ = 6.626E-34

#Constante de Planck em Ev

hEv = 4.136E-15




def main():
    entrada = input("""
Informe sua entrada:
    [1] Em -> Bm, I
    [2] Bm -> Em, I
    [3] I  -> Em, Bm
    """)


#Entradas -------------------------

def Em():
    print("")

def Bm():
    print("")

def I():
    print("")

#----------------------------------


#Conversões -----------------------
#Fator de conversão de energia: 1 eV = 1,602·10-19 J

def energiaParaEv(E):
    return E/1.602E-19

def energiaParaJ(E):
    return E*1.602E-19


#----------------------------------
