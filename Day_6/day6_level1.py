# 1. Crear una tupla vacía
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# 2. Crear tuplas con nombres de hermanas y hermanos (pueden ser imaginarios)
sisters = ("Ana", "Lucía")
brothers = ("Carlos", "Mateo")
print("Sisters:", sisters)
print("Brothers:", brothers)

# 3. Unir las tuplas de hermanas y hermanos
siblings = sisters + brothers
print("Siblings:", siblings)

# 4. ¿Cuántos hermanos tengo?
print("Number of siblings:", len(siblings))

# 5. Agregar padre y madre a la tupla de hermanos
family_members = siblings + ("Mamá", "Papá")
print("Family members:", family_members)