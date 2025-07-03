age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Convierte las edades en un conjunto y comparar su longitud.
age_set = set(age)
print("Length de list:", len(age))       
print("Length de set:", len(age_set))    

# 2. Diferencia entre string, list, tuple y set:

"""
- string: Secuencia inmutable de caracteres(e.g., "Hola mundo").
- list: Ordenado, mutable, permite duplicados (e.g., [1, 2, 3]).
- tuple: Ordenado, inmutable, permite duplicados. (e.g., (1, 2, 3)).
- set: Desordenada, mutable, sin duplicados. (e.g., {1, 2, 3}).
"""

# 3. Contar palabras únicas en una oración
Enunciado = "I am a teacher and I love to inspire and teach people"
words = Enunciado.split()
palabras_unicas = set(words)
print("Palabras_unicas :", palabras_unicas)
print("Numero de palabras unicas :", len(palabras_unicas))