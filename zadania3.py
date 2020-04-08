## zad1
# a)

A = [1/x for x in range(10) if x>0]
print(A)

# b)

B = [2**x for x in range(11)]
print(B)

print("c)")
C = [x for x in range(2**10) if x%4==0]
print(C)

## zad2


lista=[[i for i in range(1+4*j,5+4*j)] for j in range(4)]  
print(lista)
przek=[lista[x][x]for x in range(4)]
print(przek)

## zad3

produkty={"Bulka": "sztuka","Banany": "Kg","woda": "litr"}
print(produkty)
sztuki={x:"sztuka" for x in produkty}
print(sztuki)

## zad4

def monotonicznosc(a):

    if a>0:
        print("funkcja jest rosnaca")
    elif a==0:
        print("funkcja jest stala")
    else:
        print("funkcja jest malejaca")

monotonicznosc(5)

## zad5

def czyRownolegle(a1,a2):
    if a1==a2:
        print("proste sa rownolegle")
    elif a1*a2==-1:
        print("proste sa prostopadle")
    else:
        print("proste nie sa rownolegle ani prostopadle")

czyRownolegle(float(-0.5),float (2))

## zad6

import math
def dlugoscProm(x,a,y,b):
    promien=(x-a)**2+(y-b)**2
    promien=math.sqrt(promien)
    print("Promien: ",promien)
dlugoscProm(2,4,2,3)

## zad7

def pitagoras(a,b):
    c=a**2+b**2
    c=math.sqrt(c)
    print("Przeciwprostokatna: ",c)
    
pitagoras(4,5)

## zad8

def ciag(a,r,n):
    suma=(2*a+(n-1)*r)/2*n 
    print("Suma: ",suma)
ciag(2,2,15)

## zad9

def ciag2(*ciag):
    if(ciag)==0:
        return 0.0
    else:
        suma = 1.0 
        for i in ciag:
            suma = suma*i
        return suma
print(ciag2(1,3,5,7,9,11,13,15,17,19))

### zad10

def zakupy(**klucz):
    suma=0
    for i in klucz:
        suma+=klucz[i]
    print("Suma produktow :",suma)

zakupy(banany=10,jajka=4,chleb=1,bulka=5)

### zad11

from liczby_zespolone import *
x=complex(4,12)
y=complex(2,8)
print(zespolone.urojona(x), "j",sep="")
print(zespolone.urojona(y), "j",sep="")
print(dodawanie_odejmowanie.dodawanie(x,y))
print(dodawanie_odejmowanie.odejmowanie(x,y))

### zad12

from ciagi import *
print(arytm.an(2,5,10))
print(arytm.suma(1,10,15))
print(geom.an(1,4,10))
print(geom.suma(1,6,5))
