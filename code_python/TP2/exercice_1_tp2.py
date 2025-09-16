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

decision=decision_test(x,n)
print("decision =",decision)