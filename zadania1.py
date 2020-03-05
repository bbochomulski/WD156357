import math

## zad 1
zmienna1 = 3.14
zmienna2 = 3
print(zmienna1)
print(zmienna2)

## zad 2
a = int(input("Wprowadz liczbe a: "))
b = int(input("Wprowadz liczbe b: "))
suma = a + b
roznica = a - b
iloczyn = a * b
if b == 0: iloraz = "Dzielenie przez zero"
else: iloraz = a / b
modulo = a % b
potega = a ** b
print(f'Dodawanie: {suma}')
print(f'Odejmowanie: {roznica}')
print(f'Mnozenie: {iloczyn}')
print(f'Dzielenie: {iloraz}')
print(f'Reszta z dzielenia a przez b: {modulo}')
print(f'Potega: {iloraz}')

## zad3
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a **= 2
print(a)
a %= 2
print(a)

## zad4
print(math.e ** 10)
print((math.log(5+(math.sin(8)**2)))**1/6)
print(math.fabs(3.55))
print(math.fabs(4.80))

## zad5
imie = "BARTOSZ"
nazwisko = "BOCHOMULSKI"
imie = imie.capitalize()
nazwisko = nazwisko.capitalize()
print(f"{imie} {nazwisko}")

## zad6
song = "la la la la la la la"
la = song.count("la")
print(f"Ilosc powtorzen 'la': {la}")

## zad7
lancuch = "lancuch znakow"
print(f"Drugi znak: {lancuch[1]}\nOstatni znak: {lancuch[len(lancuch)-1]}")

## zad8
print(song.split())

## zad9
zmienna1 = "string"
zmienna2 = 3.14145234
zmienna3 = hex(12)
print(zmienna1)
print(zmienna2)
print(zmienna3)