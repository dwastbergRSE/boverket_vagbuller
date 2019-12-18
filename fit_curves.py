
import numpy as np
import scipy
from scipy import optimize


def logfn(x,a,b):
    return a*np.log(x)+b

ekv_ljud = {
    40: np.array([53,56,58,59,60,61,61,62,63,63,66,68,69,70]),
    50: np.array([55,58,60,61,62,63,63,64,65,65,68,70,71,72]),
    60: np.array([57,60,62,63,64,65,65,66,67,67,70,72,73,74]),
    70: np.array([59,62,64,65,66,67,67,68,69,69,72,74,75,76]),
    80: np.array([60,63,65,66,67,68,68,69,70,70,73,75,76,77]),
    90: np.array([61,64,66,67,68,69,69,70,71,71,74,76,77,78]),
    100: np.array([62,65,67,68,69,70,70,71,72,72,75,77,78,78]),
    110: np.array([63,66,68,69,70,71,71,72,73,73,76,78,79,80]),
}
ADT = np.array([1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000])


for k,v in ekv_ljud.items():
    params = scipy.optimize.curve_fit(logfn,ADT,v)[0]
    print(f"{k}: {params}")

dist = [10,50,100,150,200,250,300,350]
hard = [0,6.5,9.5,11,12.5,13.5,14,15]
soft = [0,8,15,18,21,22.5,24,25.2]
print(f"hard: {scipy.optimize.curve_fit(logfn,dist,hard)[0]}")
print(f"soft: {scipy.optimize.curve_fit(logfn,dist,soft)[0]}")