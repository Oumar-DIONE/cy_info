# Exercice 2 : Affichage de fonctions

print("Importer les modules matplotlib.pyplot et numpy.")
import numpy as np
import matplotlib.pyplot as plt 

print(" Définir la fonction ∀x ∈R, f(*) afficher la valeur de f en 0.")

def f(x):
    y=(3*np.exp(x))/(1+x**2)
    return y

x=0
y=f(x)
print("La valeur de f en  ",x,"vaut ",y)

print(" Définir la fonction ∀ t ∈ [-pi,pi], g(*) afficher la valeur de g en 0 et en pi.")
PI=3.14
def g(t,a=PI):
    if (-a<=t and t<=a):
        y1=(np.cos(t))/(1+np.sin(t)**2)
        y2=np.sin(t)*y1
    else :
        exit("t must belong to   [,",-a,a,"]")
    
    
    return (y1,y2)

t1=0
t2=PI
Y1=g(t1)
Y2=g(t2)
print("La valeur de g en  ",t1,"vaut ",Y1)
print("La valeur de g en  ",t1,"vaut ",Y2)

print("racer la courbe de la fonction f sur le segment [−5,5]")
min_x=-5
max_x=5
n_pts=30
X=np.linspace(min_x,max_x,n_pts)
Y=f(X)
print(Y)

plt.plot(X,Y)