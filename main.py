from math import *
from decimal import Decimal, getcontext

getcontext().prec = 28

#Velocidade da luz no vacuo
c = Decimal(3E8)

#Massa do eletron
me = Decimal(9.11E-31)

#Constante magnetica
𝜇0 = Decimal((4*pi)*10**-7)

#Constante de Planck em J x s
hJ = Decimal(6.626E-34)

#Constante de Planck em Ev

hEv = Decimal(4.136E-15)




def main():
    while True:
        entrada = int(input("""
Informe sua entrada:
    [1] Em -> Bm, I
    [2] Bm -> Em, I
    [3] I  -> Em, Bm
    """))
        match entrada:
            case(1):
                em = input("Em: ")
                Em(em)
            case(2):
                bm = input("Bm: ")
                Bm(bm)
            case(3):
                i = input("i: ")
                I(i)
                
#Entradas -------------------------

def Em(em):
    em = Decimal(em)
    i = (em**2)/((2 * 𝜇0) * c)
    bm = em/c
    print(f'bm = {bm:.4e} | i = {i:.4e}')

def Bm(bm):
    bm = Decimal(bm)
    em = bm * c
    i = ((c / (2 * 𝜇0)) * (bm**2))
    print(f'em = {em:.4e} | i = {i:.4e}')

def I(i):
    i = Decimal(i)
    em = sqrt(i * (2 * 𝜇0) * c)
    bm = sqrt((i * (2 * 𝜇0)) / c)
    print(f'em = {em:.4e} | bm = {bm:.4e}')

#----------------------------------


#Conversões -----------------------
#Fator de conversão de energia: 1 eV = 1,602·10-19 J

def energiaParaEv(E):
    return E/1.602E-19

def energiaParaJ(E):
    return E*1.602E-19


#----------------------------------

main()