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
zmienna1 = "napis"
zmienna2 = 3.14145234
zmienna3 = hex(12)
print(zmienna1)
print(zmienna2)
print(zmienna3)

## zad10
filmy = ["Wladca Pierscieni","Harry Potter", "Interstellar", "Incepcja"]
filmy.sort()
print("Lista filmow: ", filmy)

## zad11
sinus = [0,math.sin(math.pi/6),math.sin(math.pi/4),math.sin(math.pi/3),1]
cosinus = [1,math.cos(math.pi/6),math.cos(math.pi/4),math.cos(math.pi/3),0]
tangens = [0,math.tan(math.pi/6),1,math.tan(math.pi/3),"nie istnieje"]
cotangens = ["nie istnieje",1/(math.tan(math.pi/6)),1,1/(math.tan(math.pi/3)),0]
print("sin = ",sinus)
print("cos = ",cosinus)
print("tg = ",tangens)
print("ctg = ",cotangens)

## zad12
zdanie = "Ala ma kota a kot ma Ale"
zdanie = zdanie.split()
print(zdanie)

## zad13
slownik = {
    'ksywka1' : 'Rafal',
    'ksywka2' : 'Kacper',
    'ksywka3' : 'Michal',
    'ksywka4' : 'Bartek'
}
print(slownik['ksywka3'])
print(slownik['ksywka4'])

## zad15
rzymskie = {
    'I' : 1,
    'II' : 2,
    'III' : 3,
    'IV' : 4,
    'V' : 5,
    'VI' : 6,
    'VII' : 7,
    'VIII' : 8,
    'IX' : 9,
    'X' : 10
}
index = list(rzymskie.keys())
values = list(rzymskie.values())
print(f"Index: {index[3]}\nValue: {values[2]}")

## zad16
dict_gry = {
    '000001' : 'Gothic',
    '000002' : 'Gothic II',
    '000003' : 'Gothic III',
    '000004' : 'Arcania'
}
print(len(dict_gry))