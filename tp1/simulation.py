from matplotlib import pyplot as plt
import random as r
import math 

def simulation(Cab) :
    n = r.random()
    x = math.log(1/n)/Cab
    return x

def calcNsimulations(Cab,nbSimulations) :
    lesX = []
    for i in range(nbSimulations) :
        lesX.append(simulation(Cab))
    lesX.sort()
    return lesX 


lesX = calcNsimulations(100,10000)
plt.hist(lesX,100)
plt.show()

# print(calcNsimulations(10,1000,20,100))
    

