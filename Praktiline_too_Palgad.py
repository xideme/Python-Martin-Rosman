from Praktiline_too_PalgadFunc import *

palgad=[1200,1200,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("Lisamine-1\nKustutamine-2\nSuurimPalk-3\nSort-5\n")
    v=int(input())
    if v==1:
        k=int(input("Mitu inimest lisame? "))
        inimesed,palgad=Lisamine(inimesed, palgad,k)
        for i in range(len(palgad)):
            print(inimesed[i], "saab kätte",palgad[i])
    elif v==2:
        inimesed,palgad=Kustutamine(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif v==3:
        maxpalk,nimi=SuurimPalk(inimesed,palgad)
        print(nimi,"saab kätte",maxpalk,"Eur")
    elif v==5:
        i=int(input("Kasvab-0, Kaheneb-1\n"))
        inimesed,palgad=Sort(inimesed,palgad,i)
        for i in range(len(palgad)):
            print(palgad[i], "on", inimesed[i], "-l")


