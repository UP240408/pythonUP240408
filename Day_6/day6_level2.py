
#1.- Desempaquetar hermanos y padres
family_members = ('Ana', 'Lucía', 'Carlos', 'Mateo', 'Mamá', 'Papá')
sister1, sister2, brother1, brother2, mother, father = family_members
print("Sisters:", sister1, sister2)
print("Brothers:", brother1, brother2)
print("Mother:", mother)
print("Father:", father)


#2.- Crear tuplas de alimentos
fruits = ('Apple', 'Banana', 'Mango')
vegetables = ('Carrot', 'Spinach', 'Potato')
animal_products = ('Milk', 'Eggs', 'Cheese')

#Unir las tres tuplas
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff (tuple):", food_stuff_tp)

#3.- Convertir tupla a lista
food_stuff_lt = list(food_stuff_tp)
print("Food stuff (list):", food_stuff_lt)


#4.- Cortar el ítem o ítems del medio
length = len(food_stuff_lt)
if length % 2 == 0:
    middle_items = food_stuff_lt[length//2 - 1:length//2 + 1]
else:
    middle_items = [food_stuff_lt[length // 2]]
print("Middle item(s):", middle_items)

# 5.- Cortar los primeros 3 y los últimos 3 elementos
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First 3 items:", first_three)
print("Last 3 items:", last_three)


#6.- Eliminar completamente la tupla
del food_stuff_tp
# print(food_stuff_tp)  # Esto causaría un error si lo descomentas, porque fue eliminada


# 7.- Verificar si un elemento existe en una tupla
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Verificar Estonia
print("Is 'Estonia' a Nordic country?", 'Estonia' in nordic_countries)

# Verificar Iceland
print("Is 'Iceland' a Nordic country?", 'Iceland' in nordic_countries)