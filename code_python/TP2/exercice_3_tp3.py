# La méthode de Simpson
import numpy as np
def Factory_f():
    def f(x):
        y=np.sin(x+np.exp(x))
        return y 
    return f
def gamma(f,x,i):
    # r_i est le coef x**{i} dans le primitive de P
    r_1,r2,r_0,r_3=(1,1,1,1)
    r_2=1
    r_1=1
    r_0=1
    x1=x[i]
    x2=x[i+1]
    gam_i=r_3*(x2**3-x1**3)+r_2*(x2**2-x1**2) +r_1*(x2-x1)
    return gam_i

f=Factory_f()
j=2
x=np.linspace(0,1,9)
gam_i=gamma(f,x,j)
print("For i =",j,"gamma_i  is is worth ",gam_i)

def simpson(f,a,b,n):
    x=np.linspace(a,b,n)
    s_n=0
    for j in range(n-1):
        gam_i=gamma(f,x,j)
        s_n=s_n+gam_i
    return s_n
a,b,n=0,1,9
s_n=simpson(f,a,b,n)
print("For n = ",n," s_n is worth ",s_n)