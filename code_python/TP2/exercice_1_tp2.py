import numpy as np
def approx_ln(x,n):
    s=0
    for k in range(1,n+1):
        s=((-1)**(k))*(x**(k))/k
    return s
# e stand for precision
# x is the value at which we evaluate functions (log ang approx)
def decision_test(x,n,e=0.0001):
    y=np.log(1+x)
    y_hat=approx_ln(x,n)
    error=abs(y-y_hat)
    decision=0
    if (error<e):
        decision=1 # mean that our estimate is close to the true value at the precision e
        
    return decision

x=1/10000
n=20
import scipy as sp
decision=decision_test(x,n)
print("decision =",decision)

def test_scipy_integrate():
    def g(x):
        return x
    I, precision=sp.integrate.quad(g,0,1) 
    print("scipy integration is  ",I," should be 0.5","\n","precision",precision )
    return I 

test_scipy_integrate()



# Exercice 1 : Methode des trapèze

def Factory_f():
    def f(x):
        y=np.sin(x+np.exp(x))
        return y 
    return f
g=Factory_f()
print(g(0))

print(np.linspace(0,1,9))

def trapeze(f,a,b,n):
    X=np.linspace(a,b,n+1)
    T_n=0
    for i in range(0,n):
        x_i_1=X[i+1]
        x_i=X[i]
        y=f(x_i_1)+f(x_i)/2
        T_n=T_n+((b-a)/(2*n))*(y)
    return T_n
g= Factory_f()   
T_n=trapeze(g,a=0,b=1,n=10)
print("T_n vaut ",T_n)

def test_trapeze(f,a,b,n):
    I=sp.integrate.quad(f,a,b)
    I_hat=trapeze(f,a,b,n)
    error=abs(I-I_hat)
    return(error)

error=test_trapeze(g,a=0,b=1,n=10)
print("the error is worth   ",T_n)

res=np.logspace(2,4,num=50,endpoint=True,base=10.0)
print(res)
res_int=[int(res[i]) for i in range(0,len(res))]
print(res_int)


Y=[0  for i in range(0,len(res))]
for N in range(0,len(res)):
    error_n=test_trapeze(g,a=0,b=1,n=N)
    Y[n]=
    

    
