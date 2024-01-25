from random import *
def failist_to_dict(f:str):
    riik_pealinn={}
    pealinn_riik={}
    riigid=[]
    with open(f,'r',encoding="utf-8-sig") as file:
        for line in file:
            if '-' not in line:
                raise ValueError(f"Строка '{line.strip()}' не содержит символ '-'")
            k,v=line.strip().split('-')
            riik_pealinn[k]=v
            pealinn_riik[v]=k
            riigid.append(k)
    return riik_pealinn, pealinn_riik, riigid

riik_pealinn, pealinn_riik, riigid = failist_to_dict("RiigidPealinnad.txt")
print(riik_pealinn)
