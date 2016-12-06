from matplotlib import pyplot as plt
import random as r
import math 

def reaction(X,reaction):
    '''
    X une liste de quantités d'especes.
    reaction[0] -> liste des couples [indice,nbconsomme]
    reaction[1] -> liste des couples [indice,nbobtenus]
    '''
    reactifs = reaction[0]
    reactants = reaction[1]
    for (indice,nbconsomme) in reactifs :
        X[indice] -= nbconsomme
    for (indice,nbobtenus) in reactants :
        X[indice] += nbobtenus




def simulation(C,X,lesReactions,h) :
    '''
    C valeur de chaque reaction
    X quantite initiale de chaque espece
    lesReactions une liste de String expliquant la reaction
    h nombre de combinaisons possible des réactifs
    '''
    cardA = [X[0]]
    cardB = [X[1]]
    cardC = [X[2]]
    lesTemps = [0]
    t = 0
    n = 0
    M = len(lesReactions)
    while(True) :
        # box 1
        lesA = []
        for v in range(len(C)) :
            lesA.append(h[v].calculH(X)*C[v]) # <- h est le nombre de combinaisons
        a0 = sum(lesA)
        if a0 == 0 :
            break
        # box 2
        r1 = r.random()
        r2 = r.random()

        tau = (1/a0) * math.log(1/r1)
        
        produitTmp = r2 * a0
        decoupeA = []
        decoupeA.append(0)
        for v in range(len(C)) :
            decoupeA.append(lesA[v]+decoupeA[v])
        for v in range(len(C)) :
            if produitTmp <= decoupeA[v+1] and produitTmp > decoupeA[v] :
                mu = v
                break
        # box 3
        t += tau
        n += 1
        reaction(X,lesReactions[mu])
        lesTemps.append(t)
        cardA.append(X[0])
        cardB.append(X[1])
        cardC.append(X[2])
    plt.plot(lesTemps,cardA)
    plt.plot(lesTemps,cardB)
    plt.plot(lesTemps,cardC)


class H1(object):
    """docstring for H"""
    def __init__(self):
        super(H1, self).__init__()
        
    def calculH(self,X) :
        cardA = X[0]
        cardB = X[1]
        return cardA*cardB

class H2(object):
    """docstring for H"""
    def __init__(self):
        super(H2, self).__init__()
        
    def calculH(self,X) :
        cardB = X[1]
        cardC = X[2]
        return cardB * cardC

class H3(object):
    """docstring for H"""
    def __init__(self):
        super(H3, self).__init__()
        
    def calculH(self,X) :
        cardA = X[0]
        cardC = X[2]
        return cardA * cardC    

h1 = H1()
h2 = H2()
h3 = H3()
reaction1 = [[(0,1),(1,1)],[(1,1)]]
reaction2 = [[(1,1),(2,1)],[(2,1)]]
reaction3 = [[(0,1),(2,1)],[(0,1)]]

lesReactions = [reaction1,reaction2,reaction3]

simulation([3.3,3.3,3.4],[100,100,100],lesReactions,[h1,h2,h3])
plt.show()