it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Encontrar la longitud del conjunto it_companies
print(len(it_companies))  # Output: 7

# 2. Añadir 'Twitter' a it_companies
it_companies.add('Twitter')

# 3. Insertar varias empresas de TI a la vez
it_companies.update(['Intel', 'Cisco', 'HP'])

# 4. Eliminar una de las empresas del conjunto
it_companies.remove('Oracle') 


# 5. Diferencia entre remove() y discard()
#    - remove(): Marcara error si no existe un item.
#    - discard(): No hace nada si el item no se encuentra.