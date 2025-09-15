# Ctrl + K  puis  Ctrl + C   (pour commenter)
# Ctrl + K  puis  Ctrl + U   (pour décommenter)


# Manipulation des listes
# Question i 
l1=[]
l1.append(1)
l1.append(2)
l1.append(3)

print("voici la liste 1","\n",l1)

# Question ii
l2=[4,5,6]
print("voici la liste 2","\n",l2)

l=l1+l2

print("voici la liste l1+l2","\n",l)

v4=l[3] # attention en python les index commencznt à partir de 0
v=l[-1]
print("Afficher le quatrième élément de la liste L, puis son avant-dernier élément")
print(v4,"\n",v)
l.insert(3,8) # inserer la valeur  8 à l'index 3
print("voici la liste l1+l2","\n",l)

n=len(l)
tip=type(l)

print("quels sont la longueur et le type de la liste L?")
print(n,"\n",tip)

# print(help(list()))
# TypeError: list indices must be integers or slices, not tuple
# sequence =start:stop:step
# tuple =(a,b,c,d)

l3=l[0:5]
print('Extraire la liste L3 des cinq premiers éléments de la liste L')
print(l3)

print("Supprimer le troisième élément de la liste L3, puis le nombre 1 de la liste L3")

print("avant voici :","\n",l3)
del(l3[3])
print("maintenant  voici :","\n",l3)
print(l3)

l3.remove(1)
print("maintenant  voici :","\n",l3)
print(l3)

print('Créer une liste M des listes L1, L2 et L3')
list()
M=[l1,l2,l3]
print("voici la liste M ","\n",M)

print("afficher le troisième élément de la deuxième liste de la liste M.")
M_3=M[2]
print(M_3,"\n")
print("Concaténer la première et la dernière liste de la liste M, puis l ajouter à la fin de la liste M")
M.append(M[0]+M[-1])
print(M,"\n")
print("Quels sont la longueur et le type de la liste M?")
n=len(M)
print(type(M))

# print("There are four collection data types in the Python programming language:")
# print("List is a collection which is ordered and changeable. Allows duplicate members.")
# print("Tuple is a collection which is ordered and unchangeable. Allows duplicate members.")
# print("Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.")
# print("Dictionary is a collection which is ordered** and changeable. No duplicate members.")





