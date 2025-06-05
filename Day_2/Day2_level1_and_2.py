#Day 2: 30 Days of python programming
#Level 1
first_name = 'José Andrés'
last_name = 'Chairez Contreras'
full_name = first_name + ' ' + last_name
country = 'México'
city = 'Aguascalientes'
age = 18
is_married = False
is_true = True
is_light_on = False
Animals = ['Dog', 'Whale', 'crocodile']

#Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(Animals))

length_of_first_name = len(first_name)
print("Length of first name:", length_of_first_name)

length_of_last_name = len(last_name)
print("Length of last name:", len(last_name))

num_one= 5
num_two = 4
print("Total: ", num_one + num_two)
print("Diff: ", num_two - num_one)
print("Product: ", num_two * num_one)
print("División: ", num_one / num_two)
print("Remainder: ", num_two % num_one)
print("Exp: ", num_one ** num_two)
print("Floor_division: ", num_one // num_two)

radius_of_circle = 30 #Metros
area_of_circle = 3.14 * radius_of_circle ** 2
print("Area of circle:", area_of_circle)
circum_of_circle = 2 * 3.14 * radius_of_circle
print("Circum of circle:", circum_of_circle)

# poner el radio del circulo
input_radius = float(input("Enter the radius of the circle: "))
area_of_circle = 3.14 * input_radius ** 2
print("Area of circle:", area_of_circle)

# obtener datos del usuario
input_first_name = str(input("Enter your first name: "))
input_last_name = str(input("Enter your last name: "))
input_age = int(input("Enter your age: "))
input_country = str(input("Enter your country: "))

