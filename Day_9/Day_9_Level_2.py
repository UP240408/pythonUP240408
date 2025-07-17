# 1.-
def get_grade(score):
    if 80 <= score <= 100:
        return 'A'
    elif 70 <= score <= 79:
        return 'B'
    elif 60 <= score <= 69:
        return 'C'
    elif 50 <= score <= 59:
        return 'D'
    elif 0 <= score <= 49:
        return 'F'
    else:
        return 'Invalid score'


# 2.-
def get_season(month):
    month = month.lower()
    if month in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    elif month in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif month in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif month in ['junio', 'julio', 'agosto']:
        return 'Verano'
    else:
        return 'Mes incorrecto'


# 3.-
fruits = ['banana', 'orange', 'mango', 'lemon']

def check_and_add_fruit(new_fruit):
    new_fruit = new_fruit.lower()
    if new_fruit in fruits:
        print('That fruit already exists in the list')
    else:
        fruits.append(new_fruit)
        print('Updated fruit list:', fruits)


# Example Usage:
# Grading
score_input = int(input("Ingresa tu puntaje de estudiante: (0-100): "))
print('Tu grado es:', get_grade(score_input))

# Season
month_input = input("Ingresa un mes: ")
print('Es temporada de:', get_season(month_input))

# Fruit check
fruit_input = input("Ingresa una fruta: ")
check_and_add_fruit(fruit_input)
