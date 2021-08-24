import datetime
#Nem ismert dátum definiálása -> NI
NI = datetime.datetime(1,1,1)
class Adatok:
    def hetnapja(self,ev: int, ho: int, nap: int) -> str:
        napok: str = ["v", "h", "k", "sze","cs", "p", "szo"]
        honapok: int = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        if ho < 3 : 
            ev = ev -1
            return  napok[(ev + int(ev / 4) - int(ev / 100) + int(ev / 400 )+ honapok[ho-1] + nap) % 7]



    #6. feladat: metódus pszeudókódból
    def __init__(self, datum,nev,resz,perc,latta):
        self.datum = datetime.datetime.strptime(datum, "%Y.%m.%d") if datum!="NI" else NI
        self.nev = nev
        self.resz = resz
        self.perc = int(perc)
        self.latta = True if latta == "1" else False
        self.nap = "NI" if datum == NI else self.hetnapja(self.datum.year, self.datum.month, self.datum.day)
lista = []

#Beolvasás: növelem a sorokat egyel, és ha eléri az ötöt, betesszük az adatokként  a listába
with open("lista.txt", encoding="ISO-8859-2") as Beolvas:
    sor =0
    sorok = []
    for x in Beolvas:
        sor+=1
        sorok.append(x.strip())
        if  sor == 5:
            lista.append(Adatok(sorok[0],sorok[1],sorok[2],sorok[3],sorok[4]))
            sorok.clear()
            sor =0



#2. feladat
print(f"2. feladat:\nA listában {sum(1 for x in lista if x.datum!=NI)} db vetítési dátummal rendelkező epizód van.\n")

#3. feladat
atlag = (sum(1 for x in lista if x.latta)/len(lista))*100
print(f"3. feladat:\nA listában lévő epizódok {atlag: .2f}%-át látta.\n")

#4. feladat
ido = datetime.datetime(1,1,1,0,0,0)
ido =ido +datetime.timedelta(minutes = sum(x.perc for x in lista if x.latta))
print(f"4. feladat:\nSorozatnézéssel {ido.day-1} napot {ido.hour} órát és {ido.minute} percet töltött.")

#5. feladat
bekert = input("5. feladat:\nAdjon meg egy dátumot! Dátum= 2017.10.18: ")
bekertD = bekert.split('.')
datum = datetime.datetime(int(bekertD[0]),int(bekertD[1]),int(bekertD[2]))
valogatott = [x for x in lista if x.datum ==  datum]
[print(f"\t{x.resz}\t{x.nev}") for x in valogatott]


#7. feladat
bekertNap = input("7. feladat:\nAdja meg a hét egy napját (például cs)! Nap= cs: ")
nap = False
for x in lista: 
    if x.nap == bekertNap:
        nap =True
        print(x.nev)
if nap == False: print("Az adott napon nem került adásba sorozat.")

#8. feladat
sorozatok = {x.nev for x in lista}
eredmenyek = {}
print("8.feladat: summa.txt")
for x in sorozatok:
    perc = 0
    szam = 0
    for y in lista:
        if x ==y.nev :
            perc +=y.perc
            szam+=1
    eredmenyek[f"{x}"] = eredmenyek.get(f"{x}", [perc,szam])

with open("summa.txt", "w", encoding="ISO-8859-2") as Kiiras:   
    for x,y in eredmenyek.items():
        Kiiras.write(f"{x} {y[0]} {y[1]}\n")
        

