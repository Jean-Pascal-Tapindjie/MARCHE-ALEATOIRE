# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:10:49 2026

@author: pascal
"""
import random
import numpy as np
import matplotlib.pyplot as plt

"Marche aléatoire en une Dimension"
def PileOuFace()-> float:  #recherche une valeur aléatoire entre 0 et 1 et retourne -1 ou 1 si la valeur est >1/2 ou pas afin d'avoir équiprobabilité
    y= random.uniform (0,1)
    if y < 1/2 :
        return -1
    return 1

def Position (N: int)->int: #crée une liste de position d'une particule en marche aléatoire à chaque instant t en une dimension  
    x = 0
    i=0
    L = [x]
    for i in range (N) :
        x += PileOuFace ()
        L.append(x)
    return L
plt.title ("Marche Aléatoire une dimension")
plt.plot(Position(1000), label = "Position aléatoire")
plt.legend()

def PositionBornee():#Borne la position de la particule entre -30/+30 et limite le nombre d'itérations à 10000 
    x=0
    i=0
    L=[x]
    while i<= 10000 and x > -30 and x < 30 :
        x += PileOuFace()
        L.append(x)
        i+= 1
    return L
   
plt.plot(np.linspace(-30,-30,5000),"r--")
plt.plot(np.linspace(30,30,5000),"r--")
plt.plot(PositionBornee(), label = 'Position aléatoire bornée')
plt.legend()
plt.xlim(0,500)
plt.ylim(-50,50)
plt.grid (True)

"Marche Aléatoire en deux dimensions"

def boussole ()->(float,float): 
    y = random.uniform(0,1)
    if y < 1/4 :
        return (1,0)
    elif  y < 1/2 :
        return (-1,0)
    elif y < 3/4 :
        return (0,-1)
    else :
        return (0,1)
    
def Position2D (N: int ):
    x = 0
    y = 0
    i = 0
    X = [x]
    Y = [y]
    for i in range (N) :
        a,b = boussole ()
        x += a
        y += b
        X.append(x)
        Y.append(y)
    return X,Y

X,Y = Position2D(10000)     
plt.figure(figsize = (20, 10))
plt.title("Marche aléatoire en deux dimensions")       
plt.plot(X, Y, label = "Trajectoire") 
plt.scatter(X[0], Y[0], label = "depart")
plt.scatter (X[-1], Y[-1], label = "arrivée")
plt.legend()
plt.xlabel ("Absisses X")
plt.ylabel ("Ordonnées Y")
plt.axis ("equal")
plt.grid(True)
plt.show()
    
