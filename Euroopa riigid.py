from random import *

def failist_to_dict(f:str):   # из файла в словарь
  riik_pealinn={}             # dict {Riik:Pealinn}         
  pealinn_riik = {}           # dict {Pealinn:Riik}
  riigid=[]                # list
  file=open(f,'r',encoding="utf-8-sig")
  for line in file:
      k,v=line.strip().split('-')        #k - võti, v - väärtus
      riik_pealinn[k]=v 
      pealinn_riik[v]=k 
      riigid.append(k)
  file.close()
  return riik_pealinn, pealinn_riik, riigid

def Dict_to_files(fail:str,jarjend:list):
    f=open(fail,'w',encoding = "utf-8") # имя, параметр открытия, кодировка
    for item in jarjend:
        f.write(item+"\n")
    print("Dictionary saved!")
    f.close()

#

def show_riik_pealinn(riik_pealinn:dict,pealinn_riik:dict):
    riik=""
    pealinn=""
    print("\nSearch for pealinn (1) or riik(2) keys/value.\n")
    TmpC=int(input("Enter your choice: "))
    if TmpC==1:
        while True:
            pealinn=input("Sisesta pealinn: ")
            if (pealinn in pealinn_riik) and (pealinn != ""):
                print(pealinn_riik[pealinn])
            else:
                print("No this pealinn in list!")
                break
    elif TmpC==2:
        while True:
            riik=input("Sisesta riik: ")
            if (riik in riik_pealinn) and (riik != ""):
                print(riik_pealinn[riik])
            else:
                print("No this riik in list!")
                break

def AddDelete(riik_pealinn:dict,pealinn_riik:dict,riigid:list):
    print("\nAdd (1) or Delete(2) keys/value.\n")
    RP_list=[]
    TmpS: str
    i: int
    TmpC=int(input("Sinu valik: "))
    if TmpC == 1:
        NewRiik=str(input("Sisesta uus riik: "))
        NewPealinn=str(input("Sisesta riigi pealinn : "))
        if NewRiik in riik_pealinn:
            print("See riik juba nimikirjas!")
        else:
            riik_pealinn[NewRiik]=NewPealinn
            pealinn_riik[NewPealinn]=NewRiik
            riigid.append(NewRiik)
            RP_list=riigid                        # ina4e out of range!!!!
            for i in range(len(riigid)):
                TmpS=riigid[i]+"-"+riik_pealinn[riigid[i]]
                RP_list[i]=TmpS 
    
    elif TmpC==2:
        DelRiik=str(input("Sisesta riik kustutamiseks: "))
        if DelRiik in riik_pealinn:
            V= riik_pealinn.get(DelRiik)
            riik_pealinn.pop(DelRiik)
            pealinn_riik.pop(V)
            riigid.remove(DelRiik)
            #for i in riigid:
            #    if riigid[i]==DelRiik:

        else:
            print("See riik pole nimikirjas!")
    Dict_to_files("riigid_pealinnd.txt",RP_list)
    return riik_pealinn, pealinn_riik, riigid

def GameOfCity(riik_pealinn:dict,pealinn_riik:dict,riigid:list):
    Score: int
    TmpRiik: str
    TmpPealinn: str
    iValik: int
    i: int
    iValik=int(input("\n Vali riik_to_pealinn (1) or pealinn-to-riik (2): "))
    if iValik==1:
        #riigid.shuffle()
        Score=0
        for i in range(10):
            j=randint(0, len(riigid))
            print("Turn ",i+1,": Arve ara pealiin of " + riik_pealinn[riigid[j]]+"? \n")
            TmpRiik=input("Sinu vastus: ")
            if TmpRiik==pealinn_riik[riik_pealinn[riigid[j]]]:
                Score += 1
                print("Right vastus! ")
            else:
                print("Vale vastus!")
    elif iValik==2:
        #riigid.shuffle()
        Score=0
        for i in range(10):
            j=randint(0, len(riigid))
            print("Turn ",i+1,":Arve ara riik of pealinn " + pealinn_riik[riik_pealinn[riigid[j]]]+"? \n")
            TmpPealinn=input("Sinu vastus: ")
            if TmpPealinn==riik_pealinn[riigid[j]]:
                Score += 1
                print("Right vastus! " )
            else:
                print("Vale vastus!")
    print("Game over! Sinu score: ", Score , " from ",i+1, " turns...")



riik_pealinn,pealinn_riik,riigid=failist_to_dict("RiigidPealinnad.txt")

while True:
    print("\n")
    print("Vaata Dictionary - 1\nVaata Riik or Pealinn - 2\nAdd Riik or Pealinn - 3\nGame of city - 4\nEXIT - 5\n")
    v=int(input("Mis punkt valime?"))

    if v==1:
        print(riigid)

    elif v==2:
        show_riik_pealinn(riik_pealinn,pealinn_riik)

    elif v==3:
        AddDelete(riik_pealinn,pealinn_riik,riigid)
    elif v==4:
        GameOfCity(riik_pealinn,pealinn_riik,riigid)

    elif v==5:
        break





