from Praktiline_too_PalgadFunc import *

palgad=[1200,1200,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("Lisamine-1\nSuurimPalk-3")
    v=int(input())
    if v==1:
        k=int(input("Mitu inimest lisame? "))
        inimesed,palgad=Lisamine(inimesed, palgad,k)
        for i in range(len(palgad)):
            print(inimesed[i], "saab kätte",palgad[i])
    elif v==3:
        maxpalk,nimi=SuurimPalk(inimesed,palgad)
        print(nimi,"saab kätte",maxpalk,"Eur")

