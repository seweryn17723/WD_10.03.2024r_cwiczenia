import sys
import math



#skladnia do wykrywania bledow_1
# try:
#     a = int(input())
#     b = int(input())
#     result = a / b
#     #print(result)
# except ZeroDivisionError:
#     print("Error")
# except ValueError:
#     print("Wrong value")
# else:
#     print(result)
#from math import * #prawym, go to, implementation

#skladnia do wykrywania bledow_2
# try:
#     a = int(input())
#     b = int(input())
#     result = a / b
#     #print(result)
# except Exception:   #przy kazdym bledzie
#     print("Error")
# else:
#      print(result)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = []
#
# for i in list1:
#     list2.append(pow(i, 2))
# print(list2)
#
# list2 = [x**2 for x in list1]
# print(list2)
#
# list_3 = [3**y for y in range(0,6)] #range(od 0, do 6)
# print(list_3)
#
# list_4 = [x for x in list2 if x%2 == 1] #for z warunkiem if(nieparzyste)
# print(list_4)
#
# list_5 = [(x, y) for x in list_3 for y in list_4]       #ten sam efekt --- 1
# print(list_5)
#
# list_6 = []                                             #ten sam efekt --- 1
# for x in list_3:
#     for y in list_4:
#         list_6.append((x, y))
# print(list_6)

# s1 = {1: 2, 2: 3, 3: 4, 4: 5}
# s2 = {}
# for key, value in s1.items():   #ten sam efekt --- 2
#     s2[value] = key             #zamiana elementow klucz z wartoscia
# print(s1)
# print(s2)
#
# s3 = {v: k for k, v in s1.items()} #ten sam efekt --- 2
# print(s3)

# def rownanie_kwadratowe (a, b, c):                  #funkcja nie musi byc na poczatku programu
#     delta = b**2 - 4 * a * c
#     if delta < 0:
#         print("brak pierwiastkow")
#         return 0
#     elif delta == 0:
#         print("jedno rozwiazanie")
#         return ((-b /(2 * a)))
#     elif delta > 0:
#         print("dwa rozwiazania")
#         x1 = ((-b + math.sqrt(delta)/(2 * a)))
#         x2 = ((-b - math.sqrt(delta)/(2 * a)))
#         return x1, x2
#
# print(rownanie_kwadratowe(6, 1, 3))
# print(rownanie_kwadratowe(1, 2, 1))
# print(rownanie_kwadratowe(1, 4, 2))

# from math import *
# def dlugosc_odcinka(x1 = 1, x2 = 2, y1 = 3, y2 = 4):
#     return sqrt((x1-x2)**2 + (y1-y2)**2)
#
# print(dlugosc_odcinka())                                #wyswietlenie funkcji
# print(dlugosc_odcinka(4, 2, 6, 3))       #podajemy w kolejnsci
# print(dlugosc_odcinka(y2 = 3, x2 = 2, y1 = 3, x1 = 6))  #poza kolejnoscia_1
# print(dlugosc_odcinka(3, 5, y2 = 4, y1 = 3))     #poza kolejnoscia_2

#KONIEC #OPERACJE NA PLIKACH

# #przeniesc plik na nazwe projektu
# plik = open('tekst.txt', 'r', encoding='utf-8') #encoding - polskie znaki, r - czytanie / w - plik nie musi istniec
# znaki = plik.read(10) #wczyta 10 znakow
#
# linia = plik.readline() #odczyta cala linijke
# linie = plik.readlines() #odczyta cala zawartosc
#
# print(znaki)
# print(linia)
# print(linie)
#
# for l in linie:
#     print(l)

# plik = open('tekst1.txt', 'w', encoding='utf-8')    #doda plik  tekstowy z zawartoscia aaaaaaaaaaaaaaaaaaaa, jesli podalibysmy istniejacy plik t nadpiszemy zawartosc, a+ zamiast w mozena odczytywac i nadpisywac zawartosc
# plik.write('aaaaaaaaaaaa')
# plik.close()


# plik = open('tekst.txt', 'a+')      #w+ zamiast a+ czysci cala zawartosc
# plik.write('aaaaaaaaaaaaaaassscxcxz')
# plik.seek(105)
# znaki = plik.read(10)
# plik.close()
# print(znaki)

# with open('tekst.txt', 'r') as f:      #odczytanie zawartosci, roznica jest taka ze nie trzeba zamykac pliku, z automatu sie zamknie
#     lines = f.readlines()
# print(lines)

