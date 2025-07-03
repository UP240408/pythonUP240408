A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Union de A y B
print(A.union(B))

# 2. Encontrar la interseccion de A y de B
print(A.intersection(B))

# 3. Es A subconjunto de B
print(A.issubset(B)) 

# 4. ¿Son A y B conjuntos disjuntos?
print(A.isdisjoint(B)) 

# 5. Union de A con B y B con A
print(A.union(B))
print(B.union(A))

# 6. Diferencia simétrica entre A y B
print(A.symmetric_difference(B)) 

# 7. Borrar los conjuntos
del A
del B