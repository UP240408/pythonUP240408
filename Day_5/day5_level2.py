# Lista de edades de estudiantes
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Ordenar la lista, encontrar min y max
ages.sort()
print("Sorted ages:", ages)

min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)
print("Max age:", max_age)

# 2. Añadir min y max de nuevo a la lista
ages.append(min_age)
ages.append(max_age)
print("Ages after adding min and max again:", ages)

# 3. Encontrar la mediana
ages.sort()
length = len(ages)
if length % 2 == 0:
    median = (ages[length//2 - 1] + ages[length//2]) / 2
else:
    median = ages[length // 2]
print("Median age:", median)

# 4. Calcular el promedio
average = sum(ages) / len(ages)
print("Average age:", average)

# 5. Calcular el rango
age_range = max(ages) - min(ages)
print("Range of ages:", age_range)

# 6. Comparar abs(min - average) vs abs(max - average)
min_diff = abs(min_age - average)
max_diff = abs(max_age - average)
print("abs(min - average):", min_diff)
print("abs(max - average):", max_diff)

# -----------------------------
# Trabajando con lista de países
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# 7. País(es) del medio
length = len(countries)
if length % 2 == 0:
    middle_countries = countries[length//2 - 1:length//2 + 1]
else:
    middle_countries = [countries[length//2]]
print("Middle country(ies):", middle_countries)

# 8. Dividir en dos listas iguales (o una más en la primera si impar)
mid = (length + 1) // 2  # para dar 1 extra al primer grupo si impar
first_half = countries[:mid]
second_half = countries[mid:]
print("First half:", first_half)
print("Second half:", second_half)

# 9. Desempaquetar primeros 3 países y el resto como países escandinavos
country1, country2, country3, *scandic_countries = countries
print("First 3 countries:", country1, country2, country3)
print("Scandic countries:", scandic_countries)