#1.-
dog = {}
#2.-
dog['name'] = 'Spoky'
dog['color'] = 'Cafe'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3
#3.-
student = {
    'first_name': 'Andres',
    'last_name': 'Chairez',
    'gender': 'Hombre',
    'age': 18,
    'marital_status': 'Soltero',
    'skills': ['Python', 'Analista de sistemas'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address': 'Villa Hermosa'
}
#4.-
print("\n") 
print("La longitud de student es: ",len(student))
print("\n") 
#5-
skills = student['skills']
print("Skills: ", skills)
print("Tipos de Skills: ", type(skills))

#6.-
student['skills'].append('C++')
student['skills'].append('Javascript')

#7.-
keys_list = list(student.keys())
print("Keys :", keys_list)
print("\n") 
#8.-
values_list = list(student.values())
print("Values:", values_list)
print("\n") 
#9.-
student_items = list(student.items())
print("Student items as tuples:", student_items)
print("\n") 
#10.-
del student['marital_status']
print("Despues de borrar 'marital_status':", student)
print("\n") 
#11.-
del dog





