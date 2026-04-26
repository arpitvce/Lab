import matplotlib.pyplot as pl
import os
from typing import List

def analyse(emf:str,volume:str)->dict:
    try:
        if not emf:
            raise ValueError("Input is empty")
        if not volume:
            raise ValueError("Input is empty")
        arr=[]
        emf=list(map(float,emf.split(',')))
        volume=list(map(float,volume.split(',')))
        if len(emf)!=len(volume):
            raise ValueError("Length Mismatch")
        if len(emf)<2:
            raise ValueError("Only One Value Passed")
        for i in range(len(emf)-1):
            val=(emf[i+1]-emf[i])/(volume[i+1]-volume[i])
            arr.append(val)
        index=arr.index(max(arr))
        equivalence_point=(volume[index]+volume[index+1])/2
        pl.figure()
        pl.plot(volume,emf)
        pl.axvline(equivalence_point,linestyle="--",label=f"Equivalence Point{equivalence_point:.2f}")
        pl.xlabel("Volume")
        pl.ylabel("EMF")
        pl.grid()
        pl.savefig("/static/graph.png")
        pl.show()
        pl.close()
        return {"Equivalence Point":equivalence_point,"dE/dV":arr}

    except ZeroDivisionError:
        return{"Error":"No Two Values Of Volumes Can Be Same"}
    except ValueError as e:
        return{"Error":str(e)}


