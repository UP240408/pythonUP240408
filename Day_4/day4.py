#1.-
palabra = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(palabra)
print("La palabra junta dice: ",result)
#2.-
palabra = ['Coding', 'For' , 'All']
result = ' '.join(palabra)
print("La palabra junta dice: ",result)
#3.-
compañia = "Coding For All"
#4.-
print("Print de compañia: ",compañia)
#5.-
long = len(compañia)
print("La longitud de la variable compañia es ",long)
#6.-
compañia_mayus = compañia.upper ()
print("El texto en mayusculas es: ",compañia_mayus)
#7.-
compañia_lower = compañia.lower ()
print("El texto en minusculas es: ",compañia_lower)
#8.-
cap   = compañia.capitalize()
Title = compañia.title()
swarp = compañia.swapcase()

#9.-

cortar = compañia.find(" ")
texto_cortado = compañia[cortar + 1:]
print("El texto cortado nos da: " ,texto_cortado)  
#10.-
Encontrar = compañia.find("Coding")
if Encontrar != -1:
    print("Se ha encontrado coding en el texto")
else :
    print("No se encontro coding")
#11.-
Encontrar = compañia.find("Coding")
Remplazado = compañia.replace("Coding","Python")
print("El texto remplazado se vera asi: ",Remplazado)
#12.-
Python = "Python for Everyone"
Encontrarp = Python.find("Everyone")
Remplazadop = Python.replace("Everyone","All")
print("El texto remplazado se vera asi: ",Remplazadop)
#13.-
separado = compañia.split()
print("El texto separado es: ",separado)
#14.-
Empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
separado = Empresas.split(",")
print("El texto separado es: ",separado)
#15.-
print("La primera posicion en compañia es: ",compañia[0])
#16.-
print("La ultima posicion en compañia es: ",compañia[-1])
#17.-
print("En la pocision index(10) se encuentra:", compañia[10])
#18.-
words = Python.split()
acronym = ''.join(word[0] for word in words).upper()
print("El acronimo es: ",acronym)
#19.-
words = compañia.split()
acronym = ''.join(word[0] for word in words).upper()
print("El acronimo es: ",acronym)
#20.-
posicion = compañia.index('C')
print("La posicion en la que aparece C por primera vez es: ", posicion)
#21.-
posicion = compañia.index('F')
print("La posicion en la que aparece F por primera vez es: ", posicion)

#22.-
posicion = compañia.rfind('l')
print("La posicion en la que aparece L por ultima vez es: ", posicion)

#23.-
frase = "You cannot end a sentence with because because because is a conjunction"
posicion = frase.index('because')
print("La posicion en la que aparece 'because' por primera vez es: ", posicion)
#24.-
posicion = frase.rindex('because')
print("La posicion en la que aparece 'because' por ultima vez es: ", posicion)

#25.-
comienzo = frase.find('because because because')
fin = comienzo + len('because because because')
phrase = frase[comienzo:fin]
print("La frase es: ", phrase)
#26.-
posicion = frase.index('because')
print("La posicion en la que aparece 'because' por primera vez es: ", posicion)

#27.-
comienzo = frase.find('because because because')
fin = comienzo + len('because because because')
phrase = frase[comienzo:fin]
print("La frase es: ", phrase)

#28.-
si = compañia.startswith('Coding')
if si==True:
    print("Si empieza por Coding")
else:
    print("No empieza por Coding")

#29.-
si = compañia.endswith('coding')
if si==True:
    print("Si termina por coding")
else:
    print("No termina por coding")

#30.-
texto = '   Coding For All      '
resultado = texto.strip()
print(resultado)
#31.-
var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'

print("El valor de 30DaysOfPython es: ",var1.isidentifier())  
print("El valor de thirty_days_of_python es: ",var2.isidentifier())  
#32.-
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' # '.join(libraries)
print(result)
#33.-
text = "I am enjoying this challenge.\nI just wonder what is next."
print(text)
#34.-
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
#35.-
radius = 10
area = 3.14 * radius ** 2
message = "The area of a circle with radius {} is {} meters square.".format(radius, int(area))
print(message)
#36.-
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))  # Resultado con 2 decimales
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))