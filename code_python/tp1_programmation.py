## Exercice 2 : Affichage de fonctions
import numpy as np 
import matplotlib.pyplot as plt 

def f (x):
    v=3*np.exp(x)/(1+x**2)
    return v

x=0
f_at_x = f(x)
print("la valeur de f en 0 vaut ",f_at_x)

PI=3.14
def g (t,a=-PI,b=PI):
    if (t<a or b<t):
        print("t n'est pas sur le domaine de f ")
        exit()
    else:
        v1=np.cos(t)/(1+np.sin(t)**2)
        v2=(np.cos(t)*np.sin(t))/(1+np.sin(t)**2)
    v=(v1,v2)
    return v

t1=0
t2=PI
g_at_t1 = g(t1)
g_at_t2 = g(t2)

print("la valeur de g en ",t1," vaut ",g_at_t1)
print("la valeur de g en ",t2," vaut ",g_at_t2)

## Tracer la courbe de la fonction f sur le segment [−5,5]