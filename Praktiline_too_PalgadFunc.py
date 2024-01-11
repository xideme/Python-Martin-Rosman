
def Lisamine(i:list,p:list,k:int):
    """Andmete lisamine listidesse
    Tagastab listud
    ...
    :param list i: Inimeste nimekiri
    :param list p: Palkade loetulu
    :param int k: Inimeste kogus
    :rtype list, list
    """
    for _ in range(k):
        nimi=input("Mis on inimese nimi?")
        palk=int(input("Kui suur palk tal on?"))
        i.append(nimi)
        p.append(palk)
    return i,p

def SuurimPalk(i:list,p:list):
    """

    """

    nimi_list=[]
    max_=max(p)
    p.count(max_)
    #kogus=p.count(max_)

    for palk in p:
        if palk==max_:
            ind=p.index(max_,a)
            nimi=i[ind]
            a+=1
            nimi_list.append(nimi)
    return max_,nimi_list

def MinPalk(i:list,p:list):
    """

    """

    nimi_list=[]
    min_=min(p)
    p.count(min_)
    #kogus=p.count(max_)

    for palk in range(p):
        if palk==min_:
            ind=p.index(min_,a)
            nimi=i[ind]
            a+=1
            nimi_list.append(nimi)
    return min_,nimi_list

def Sort(i:list,p:list,a:int):
    """
    """
    N=len(i)
    if a==1:
        for n in range(0,N):
            for m in range (n,N):
                if p[n]<p[m]:
                    kaust=p[n]
                    p[n]=p[m]
                    p[m]=kaust
                    kaust=i[n]
                    i[n]=i[m]
                    i[m]=kaust
    else:
        for n in range(0,N):
            for m in range (n,N):
                if p[n]>p[m]:
                    kaust=p[n]
                    p[n]=p[m]
                    p[m]=kaust
                    kaust=i[n]
                    i[n]=i[m]
                    i[m]=kaust
    return i,p

def Kustutamine(i:list,p:list):
    """
    """
    nimi=input("Nimi: ")
    n=i.count(nimi)
    if n>0:
        for x in i:
            if x==nimi:
                ind=i.index(x)
                i.remove(x)
                p.pop(ind)
    else:
        print(nimi, "ei old nimikirjas")
    return i,p