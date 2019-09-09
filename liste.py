#!/usr/bin/env python3
# coding=utf-8
#pipe to sort -k2 -n -t: for sorting by points

import glob;
import csv;

listen = glob.glob('blatt*');

anzahlAufgaben = 4 * len(listen)-1

def toNumber(x):
    try:
        return float(x)
    except ValueError:
        return 0

def anzahlBearbeitet(punkte):
    anzahl = 0
    for x in punkte:
        if(x)> 0:
            anzahl = anzahl + 1
    return anzahl

summe = {}
aktiv = {}
nn = {"asdf":"qwer"}
for name in listen:
    with open(name, 'r') as f:
        freader = csv.reader(f)
        for zeile in freader:
            if zeile != []:
                nachname = zeile[0].strip()
                vorname =  zeile[1].strip()
                punkte = list(map(toNumber, zeile[2:]))
                bearbeitet = anzahlBearbeitet(list(punkte))
                punkte = sum(punkte)
                if (vorname,nachname) in summe:
                    summe[(vorname,nachname)] += punkte
                    aktiv[(vorname,nachname)] += bearbeitet
                else:
                    summe[(vorname,nachname)] = punkte
                    aktiv[(vorname,nachname)] = bearbeitet


total = 0
inaktiv = 0
personen = len(summe) - inaktiv
soll = (10+18+11*20)*0.5
print(soll)
for name in summe:
    erfolg = summe[name] >= soll
    total += summe[name]
    teilnahme = aktiv[name] > 0.75 * anzahlAufgaben
    #print nn[name] +", " + name + ", " + str(erfolg) + ", " +str(teilnahme)
    #print name + " :" +str(summe[name]) + " " + str(summe[name] - soll) + str(erfolg) + str(teilnahme)
    print(str(name[0]) + "," + str(name[1]) + " :" +str(summe[name]) + " " + str(summe[name] - soll))
    #if not(erfolg):
    #   print(str(name[1]) + ", " + str(name[0]))

print(total/personen)
