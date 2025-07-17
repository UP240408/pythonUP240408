#1.-
age = int(input("Ingresa tu edad: "))
if age >= 18:
    print("Tienes la edad suficiente para conducir.")
else:
    years_left = 18 - age
    print(f"Tu necesitas {years_left} {'años mas' if years_left > 1 else ''} Para aprender a conducir.")

print()

#2.-
my_age = 18
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    print(f"Tu tienes {diff} año{'s' if diff > 1 else ''} mas que yo.")
elif your_age < my_age:
    diff = my_age - your_age
    print(f"Yo tengo {diff} año{'s' if diff > 1 else ''} mas que tu.")
else:
    print("Tenemos la misma edad.")

print() 

#3.-
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} Es mayor que {b}")
elif a < b:
    print(f"{a} Es mas pequeño que {b}")
else:
    print(f"{a} Es igual {b}")