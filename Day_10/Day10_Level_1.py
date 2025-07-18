#1.- Usando for 
for i in range(11):
    print(i)
print()
# Usando while 
i = 0
while i <= 10:
    print(i)
    i += 1
print()
#2.- Usando for 
for i in range(10, -1, -1):
    print(i)
print()
# Usando while 
i = 10
while i >= 0:
    print(i)
    i -= 1
print()
#3.-
for i in range(1, 8):
    print('#' * i)
print()
#4.-
for i in range(8): 
    for j in range(8): 
        print("#", end=" ")
    print()
print()
#5.-
for i in range(11):
    print(f"{i} x {i} = {i * i}")
print()
#6.-
tech_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in tech_list:
    print(item)
print()
#7.-
for i in range(0, 101):
    if i % 2 == 0:
        print(i)
print()
#8.-
for i in range(0, 101):
    if i % 2 != 0:
        print(i)
print()