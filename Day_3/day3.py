age = int
height = float
that_store = complex
import math

#Area de un triangulo
print("Calculo para el area de un triangulo")
print("Ingresa la base del triangulo")
Base = int(input(""))
print("Ingresa la altura del triangulo")
Altura = int(input(""))
Area = (Base*Altura)/2
print("El area del triangulo es = ",Area)
print(" ")

#Perimetro de un triangulo
print("Calcular el perimetro de un triangulo")
Lado_a = int(input("Ingresa el lado a "))
Lado_b = int(input("Ingresa el lado b "))
Lado_c = int(input("Ingresa el lado c "))
Perimetro = Lado_a+Lado_b+Lado_c
print("El Perimetro del triangulo es = ",Perimetro)
print(" ")

#Area de un rectangulo
print("Calculo para el area de un rectangulo")
print("Ingresa la base del rectangulo")
Base = int(input(""))
print("Ingresa la altura del rectangulo")
Altura = int(input(""))
Area = (Base*Altura)
print("El area del rectangulo es = ",Area)
print(" ")

#Perimetro de un rectangulo
print("Calcular el perimetro de un rectangulo")
Lado_b = int(input("Ingresa el lado a "))
Lado_a = int(input("Ingresa el lado b "))
Perimetro = 2*(Lado_a+Lado_b)
print("El Perimetro del rectangulo es = ",Perimetro)
print(" ")

#Area de un circulo
print("Calculo para el area de un circulo")
print("Ingresa el radio del circulo")
Radio = int(input(""))
Area = 3.14*(Radio**2)
print("El area del rectangulo es = ",Area)
print(" ")

#Circunferencia de un circulo
print("Calcular la cicunferencia de un circulo")
Radio = int(input("Ingresa el lado a "))
Circ = 2*3.14*Radio
print("La circunferencia es = ",Circ)
print(" ")

#Interseccion de dos puntos
print("Encontrar la interseccion de Y ")
print("Ingresa el valor de X")
X = int(input(""))
Y = 2*X-2
print("El valor de  Y = ",Y)
print(" ")

#Pendiente
print("Calcular pendiente y distancia Euclideana entre los puntos")
print("(2,2) y (6,10)")
y1 = 2
y2 = 10
x1 = 2
x2 = 6
Pendiente = (y2-y1)/(x2-x1)
print("La La pendiente es = ",Pendiente)
eucli = math.sqrt(((y2-y1)**2)+((x2-x1)**2))
eucli = eucli
print("y la distancia euclidiana es = ",eucli)
print(" ")

#Calcular el valor de Y
print("Encontrar el valor de Y ")
print("Ingresa el valor de X")
X = int(input(""))
Y = 2*X-2
print("El valor de  Y = ",Y)
print(" ")

#Establecer x hasta que y = 0
def f(x):
    return x**2 + 6*x + 9
print(" ")

# Probar varios valores de x
for x in range(-10, 5):  # Probamos desde -10 hasta 4
    y = f(x)
    print(f"x = {x}, y = {y}")
    if y == 0:
        print(f" y es 0 cuando x = {x}")
print(" ")

#Encontrar el tamaño de dragon y python y compararlo
len_python = len('python')
print("La longitud de python es = ", len_python)
len_dragon = len('dragon')
print("La longitud de dragon es = ", len_dragon)

comparacion = len('python') != len('dragon')
print("La diferecia entre los dos es: ",comparacion)
print(" ")

#Verificar si se encuentra on en python y dragon
realpy = 'on' in 'python'and 'on' in 'dragon'
print("Se encontro on en python y dragon? = ",realpy)
print(" ")

#Ver si jargon se encuentra en este enunciado
sentence = "I hope this course is not full of jargon"
result = 'jargon' in sentence
print("En la frase 'I hope this course is not full of jargon' se encontro jargon? ",result)
print(" ")

#No se encuentra "on" en python y dragon?
realpy = not ('on' in 'python' and 'on' in 'dragon')
print("No se encuentra 'on' en python y dragon = ",realpy)
print(" ")

#Encontrar la longitud de texto de "python" y volverlo float y luego a string
texto = "python"
long = len(texto) 
long_float = float(long)
print("Su longitud es de ",long_float," letras(float)")

long_str = str(long_float)
print("Su longitud es de ",long_str," letraas(string)")
print(" ")

#Comprobar si un numero es divisible por 2 y su resultado da 0

numero= int(input("Ingrese un numero para comprobar si es divisible entre dos y da 0 de resultado: "))

if numero % 2 == 0:
    print("Si es divisible")
else:
    print("No es divisible")
print(" ")

#Vamos a verificar si la división entera de 7 entre 3 es 
# igual al valor entero de 2.7 convertido con int
result = 7 // 3 == int(2.7)
print("El resultaso de la division entera de 7 y 3 es 2.7? ",result)
print(" ")

#Verificar si '10' es igual a 10
print("'10' y 10 son iguales?")
print(type('10') == type(10))
print(" ")

#Verificar si int('9.8' es igual a 10)
print("int(9.8) y 10 son iguales?")
resultado = int(float('9.8')) == 10
print(resultado)
print(" ")

#Horas y ratio por horas
print("Conocer sus ingresos semanales")
hours = float(input("Ingrese las horas: "))
rate_per_hour = float(input("Ingrese el ratio por hora: "))
pay = hours * rate_per_hour

print("Tus ingresos semanales son: ", pay ," Pesos")
print(" ")

#Calcular los segundos de vida de una persona con sus años
years = int(input("Ingrese el numero de años que vivio: "))
segundos = years * 365 * 24 * 60 * 60

print("Tu has vivido por " ,segundos, "segundos.")
print(" ")

#Tabla
print("Tabla de numeros")
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)