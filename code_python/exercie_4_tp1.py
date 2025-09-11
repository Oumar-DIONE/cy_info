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

    u_n=compute_f_n(n)
    u_n_plus_1=compute_f_n(n+1)
    if (u_n != 0):
        r_n=u_n_plus_1/u_n
        return r_n
    else :
        exit("ratio is not defined")


r_n=compute_ratio(n)
print( "Pour n =  ",n, "le ratio vaut ",r_n)
    

    



