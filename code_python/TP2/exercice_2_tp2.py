import numpy as np 
import scipy as sp
def montecarlo(f,a,b,n):
    X=a+(b-a)*np.random.random(n)
    M_n=0
    for i in range(0,n):
        M_n=M_n+((b-a)/n)*f(X[i])

    V_n=0
    for j in range(0,n):
        V_n=V_n+((b-a)**2/n)*((f(X[i])-(M_n/(b-a)))**2)
    return M_n,V_n


def Factory_f():
    def f(x):
        y=np.sin(x+np.exp(x))
        return y 
    return f
g=Factory_f()

def Factory_f_square():
    def f(x):
        y=np.sin(x+np.exp(x))
        return y*y 
    return f
g=Factory_f()
g_square=Factory_f_square()



m_n,v_n=montecarlo(g,0,1,10)
print("m_n",m_n,"\n")
print("v_n",v_n)

print ("calcul de M_inf et V_inf")

M_inf, precision_M=sp.integrate.quad(g,0,1)
V_inf, precision_V=sp.integrate.quad(g_square,0,1)
V_inf=V_inf-(M_inf**2)


print("M_inf",M_inf,"\n")
print("V_inf",V_inf)

# grid_n est grille de valeur de N allant de 1 à 10^5 au pas logarithmique 
n_pts=int(50)
grid_n=np.logspace(0,5,num=n_pts,endpoint=True,base=10.0)
print(grid_n)
grid_n=[int(grid_n[i]) for i in range(n_pts)]
list_M_n=[]
list_V_n=[]
list_error_n=[]


for i in range(len(grid_n)):
    N=grid_n[i]
    M_n,V_n=montecarlo(g,0,1,N)
    list_M_n.append(M_n)
    list_V_n.append(V_n)
    list_error_n.append(np.sqrt(N)*abs(M_n-M_inf))
print("end ")

print("vecter des residus",list_error_n)







