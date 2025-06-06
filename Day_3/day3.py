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

#Calcular el valor de Y
print("Encontrar el valor de Y ")
print("Ingresa el valor de X")
X = int(input(""))
Y = 2*X-2
print("El valor de  Y = ",Y)
print(" ")

#Establecer x hasta que y = 0
def xif():
x = int(input("Ingresa el valor de X = "))
Y1 = x**2 + 6(x) + 9
if Y1 = 0
print("El valor de x para el que y es igual a 0 es:", x)
else(return xif) 

