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

Pi = Decimal(str(2*pi))


def main():
    print("""
     ______________________________________________
    | Artur Chaves Paiva       - RA: 22.223.023-7  |
    | Giovanni Antonio Moreira - RA: 22.223.010-4  |
    | Leonardo Souza de Castro - RA: 22.123.114-5  |
    |______________________________________________|                                       

Esse programa tem o intuito de calcular algumas propriedades de ondas e campos eletromagnéticos, e usa de diversas fórmulas para um cálculo preciso e eficiente. O programa aceita
como entrada números em notação cíentifica, usando a notação 1.23E2 (1.23²). Além disso, estamos utilizando a biblioteca decimal para maior precisão nas respostas e operações. 
""")
    while True:
        entrada = int(input("""
Informe sua entrada:
    [1] Em -> Bm, I
    [2] Bm -> Em, I
    [3] I  -> Em, Bm
--------------------------
    [4] f -> λ, k, w
    [5] λ -> f, k, w
    [6] w -> f, λ, k
    [7] k -> f, λ, w
--------------------------
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
            case(4):
                f = input("f: ")
                F(f)
            case(5):
                l = input("λ: ")
                L(l)
            case(6):
                w = input("w: ")
                W(w)
            case(7):
                k = input("k: ")
                K(k)
                
#Entradas -------------------------

def Em(em):
    em = Decimal(em)
    i = (em**2)/((2 * 𝜇0) * c)
    bm = em/c
    print(f'Bm (Campo Magnético) = {bm:.4e} T | I (Intensidade) = {i:.4e} W/m²')

def Bm(bm):
    bm = Decimal(bm)
    em = bm * c
    i = ((c / (2 * 𝜇0)) * (bm**2))
    print(f'Em (Campo Elétrico) = {em:.4e} V/m | I (Intensidade) = {i:.4e} W/m²')

def I(i):
    i = Decimal(i)
    em = sqrt(i * (2 * 𝜇0) * c)
    bm = sqrt((i * (2 * 𝜇0)) / c)
    print(f'Em (Campo Elétrico) = {em:.4e} V/m | Bm (Campo Magnético) = {bm:.4e} T')

def F(f):
    f = Decimal(f)
    l = c/f #Valor de lambda calcualdo por velocidade da luz / frequencia

    w = Pi*f #W (Numero da onda) -> 2 vezes PI vezes a frequencia

    k = w/(l*f) # K (Frequencia angular) -> w dividido por (lambda vezes a frequencia)

    print(f"λ = {l:.4e} m | k (Número de onda) = {k:.4e} rad/m | w (Frequência angular) = {w:.4e} rad/s")

def W(w):
    w = Decimal(w)

    f = w/Pi

    l = c/f

    k = w/(l*f) # K -> w dividido por (lambda vezes a frequencia)

    print(f"f = {f:.4e} Hz | λ = {l:.4e} m | k (Número de onda) = {k:.4e} rad/m")

def K(k):
    k = Decimal(k)

    l = Pi/k

    f = c/l

    w = l*f*k

    print(f"f = {f:.4e} Hz | λ = {l:.4e} m | w (Frequência angular) = {w:.4e} rad/s")

def L(l):
    l = Decimal(l)

    k = Pi/l

    f = c/l

    w = l*f*k

    print(f"f = {f:.4e} Hz | k (Número de onda) = {k:.4e} rad/m | w (Frequência angular) = {w:.4e} rad/s")

#----------------------------------


#Conversões -----------------------
#Fator de conversão de energia: 1 eV = 1,602·10-19 J

def energiaParaEv(E):
    return E/1.602E-19

def energiaParaJ(E):
    return E*1.602E-19


#----------------------------------


main()