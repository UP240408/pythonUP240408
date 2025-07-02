#1
lst = list()
#2
lst2 = ['Pino','Arce','Arbol','Alto','Largo','Platanero','Cactus']
#3
print(len(lst2))
#4
first_item = lst2[-7]
print(first_item)
middle_item = lst2[-4]
print(middle_item)
final_item = lst2[-1]
print(final_item)
#5
mixed_data_types = ['Jose_Andres', '18', '181', 'single', 'Ags']
#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM, Oracle','Amazon']
#7
print(it_companies)
#8
print("Número de empresas:", len(it_companies))
#9
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print("First company:", first_company)
print("Middle company:", middle_company)
print("Last company:", last_company)
#10
it_companies[0] = 'Meta'
print("Lista modificada:", it_companies)

#11
it_companies.append('Intel')
print("After adding a company:", it_companies)
#12
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Spotify')
print("Despues de insertarlo en el medio:", it_companies)
#13
for i in range(len(it_companies)):
    if it_companies[i].upper() != 'IBM':
        it_companies[i] = it_companies[i].upper()
        break 
print("Despues de cambiar a mayusculas :", it_companies)
#14
joined_companies = '#; '.join(it_companies)
print("Despues de unirlas :", joined_companies)
#15
check = 'Google'
if check in it_companies:
    print(f"{check} Se encuentra en la lista.")
else:
    print(f"{check} No se encuentra en la lista.")
#16
it_companies.sort()
print("Sorted list:", it_companies)
#17
it_companies.reverse()
print("Reversed list:", it_companies)
#18
first_three = it_companies[:3]
print("First 3 companies:", first_three)

#19
last_three = it_companies[-3:]
print("Last 3 companies:", last_three)
#20
length = len(it_companies)
if length % 2 == 0:
    middle = it_companies[length//2 - 1 : length//2 + 1]
else:
    middle = [it_companies[length // 2]]
print("Middle company/companies:", middle)
#21
it_companies.pop(0)
print("After removing the first company:", it_companies)
#22
length = len(it_companies)
if length % 2 == 0:
    del it_companies[length//2 - 1 : length//2 + 1]
else:
    del it_companies[length // 2]
print("After removing middle company/companies:", it_companies)
#23
it_companies.pop()
print("After removing the last company:", it_companies)

#24
it_companies.clear()
print("After removing all companies:", it_companies)
#25
del it_companies
#Aqui no funcionaria debido a que no hay una lista
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print("Nueva lista es :", full_stack)
#27
index_redux = full_stack.index('Redux')
full_stack.insert(index_redux + 1, 'Python')
full_stack.insert(index_redux + 2, 'SQL')
print("Despues de insertarlo:", full_stack)