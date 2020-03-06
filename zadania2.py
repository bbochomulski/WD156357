## zad1
ciag = input()
print(ciag.count(" "))

## zad2
import sys
print("Podaj dwie wartosci:")
war1 = int(sys.stdin.readline())
war2 = int(sys.stdin.readline())
iloczyn = war1 * war2
print("Wynik mnozenia: ")
sys.stdout.write(str(iloczyn))

## zad4
liczba = int(input("\nPodaj liczbe calkowita: "))
liczba = abs(liczba)
print(f"Wartosc bezwzgledna liczby: {liczba}")

## zad5
a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
c = int(input("Podaj liczbe c: "))
if (a>0 and a<=10) and (a>b or b>c):
    print("Warunki spelnione")
else:
    print("Warunki niespelnione")

## zad6
print("Liczby podzielne przez 5: ")
for x in range(5,55,5):
    print(str(x), end = ' ')
print("\n")

## zad7
for x in range(1,6,1):
        n = int(input("Podaj liczbe: "))
        n = n ** 2
        print(f"Kwadrat liczby: {n}")
print("\n")

## zad8
lista = []
while(len(lista) != 5):
    lista.append(int(input("Podaj liczbe:")))
else:
    print(lista)

## zad9
suma = 0
liczba = input("Podaj liczbe wielocyfrowa: ")
for x in range(0,len(liczba),1):
    suma += int(liczba[x])
print(f"Suma cyfr: {suma}")

## zad10
n = int(input("Podaj wysokosc choinki(max 10): "))
for x in range(0,n+1,1):
    for y in range(0,x,1):
        print("A", end='')
    print("")
        

## zad11
n = int(input("Podaj wysokosc diamentu(w przedziale 3-9): "))

for a1 in range(1, (n+1)//2 + 1):
    for a2 in range((n+1)//2 - a1):
        print(" ", end = "")
    for a3 in range((a1*2)-1):
        print("*", end = "")
    print()

for a1 in range((n+1)//2 + 1, n + 1):
    for a2 in range(a1 - (n+1)//2):
        print(" ", end = "")
    for a3 in range((n+1 - a1)*2 - 1):
        print("*", end = "")
    print()

## zad12
for x in range(1,11,1):
    for y in range(1,11,1):
        print(x*y,end = " ")
    print()

## zad14
while(1):
    try:
        import math
        n = int(input("Podaj liczbe: "))
        n = math.sqrt(n)
        print(f"Pierwiastek: {n}")
        break
    except ValueError:
            print ("Nie istnieje pierwiastek z liczby ujemnej!")

## zad15
while(1):
    try:
        n = int(input("Podaj liczbe: "))
        print(f"Podana liczba: {n}")
        break
    except ValueError:
        print("Prosze podac liczbe!")