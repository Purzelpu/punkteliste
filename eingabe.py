import readline
from functools import partial
import sys

namen = []
gruppen = []

#Autovervollst fur Namen
def completerN(text, state):
    options = [i for i in [name[0] for name in namen] if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

#Autovervollst fur Vornamen
def completerV(name, text, state):
    options = [i for i in [n[1] for n in namen if n[0] == name] if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

# Namensliste einlesen (Gruppen/Autovervollst)
gruppe = []
with open("namen", "r") as f:
    for zeile in f:
        if len(zeile) > 1:
            zeile = zeile.strip()
            zeile = zeile.split(",")
            nachname = zeile[0].strip()
            vorname = zeile[1].strip()
            namen.append((nachname, vorname))
            gruppe.append((nachname, vorname))
        else:
            gruppen.append(gruppe)
            gruppe = []
gruppen.append(gruppe)

# print(namen)
# print(gruppen)

zettel = input("Zettel: ")
anzahlAufgaben = int(input("Anzahl Aufgaben: "))

# Namen einlesen mit Autversollst.
readline.parse_and_bind("tab: complete")
readline.set_completer(completerN)
name = input("Nachname: ")
while name != '':
    readline.set_completer(partial(completerV,name))
    vorname = input("Vorname: ")

    #Punkte einlesen
    punkte =""
    print("Punkte zeilenweise, strg+d zum Beenden")
    for i in range(anzahlAufgaben):
        line = input("Aufgabe " + str(i+1) + ": ")
        line = line.strip()
        punkte += ", " + line

    #Passende Gruppe suchen
    G = [gruppe for gruppe in gruppen if (name, vorname) in gruppe]
    gruppe = G[0]
    gruppen.remove(gruppe)

    with open("blatt"+zettel, "a") as f:
        for name in gruppe:
            zeile = name[0] + ", " + name[1]
            namen.remove((name[0],name[1]))
            print(zeile + punkte)
            f.write(zeile + punkte + "\n")
        f.write("\n")



    readline.set_completer(completerN)
    name = input("Name: ")

print("Nicht bepunktet: ")
print(namen)
