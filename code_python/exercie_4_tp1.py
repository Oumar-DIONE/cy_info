# Importation et constantes definitions
import numpy as np 

# Définir une fonction compute_fibonacci(n) qui retourne les n premiers éléments de la
# suite de Fibonacci .

def compute_fibonacci(n):
    my_l=[]
    for i in range(0,n):
        my_l.append(compute_f_n(i))
    return my_l

def compute_f_n(n):
    if (n==0 or n==1):
        v_n=1
        return(v_n)
    else  :
        v_n=compute_f_n(n-1)+compute_f_n(n-1)
        return(v_n)
    
n=5
my_list=compute_fibonacci(n)
print( "la liste des ",n, "premiers elts de la suite de Fibonacci vaut ",my_list)
    
     
 
def compute_ratio(n):

    U_n=compute_f_n(n)
    U_n_plus_1=compute_f_n(n+1)
    if (u_n != 0):
        r_n=U_n_plus_1/U_n
        return r_n
    else :
        exit("ratio is not defined")


r_n=compute_ratio(n)
print( "Pour n =  ",n, "le ratio vaut ",r_n)


N=50
ratio_n=[]
for  n in range(0,N):
     print("calcul du ration à l'itération",n)
     r_n=compute_ratio(n)
     ratio_n.append(r_n)
    
print("la liste des ratios est : ",ratio_n)

error_n=ratio_n[-1]-1.618
print("l'erreur absolue vaut à l'indice   : ",n, "vaut ",error_n)



    

for  n in range(0,N+2):
     print("calcul du ration à l'itération",n)
     r_n=compute_ratio(n)
     ratio_n.append(r_n)
    
print("la liste des ratios est : ",ratio_n)

# Determination numérique d la valeur de p ; pour un  N numériquement trés grand .
p=ratio_n[-1] /np.log(N/(N+1))  
print("numeriquement la valeur de p vaut à peu près ",p)



U_n=compute_f_n(N)
c=  U_n*np.exp(p*np.log(N))
print("numeriquement la valeur de c vaut à peu près ",c)





