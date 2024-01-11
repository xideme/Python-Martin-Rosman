
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
    max_list=[]
    nimi_list=[]
    max_=max(p)
    p.count(max_)
    kogus=p.count(max_)
    for x in range(kogus):
        ind=p.index(max_)
        nimi=i[ind]
        nimi_list.append(nimi)
    return max_,nimi_list