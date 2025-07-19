#1.-
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [x for x in numbers if x <= 0]
print(filtered)  

#2.-
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist in list_of_lists for inner in sublist for num in inner]
print(flattened)  

#3.-
tuples_list = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print(tuples_list)

#4.-
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
formatted = [[country.upper(), country[:3].upper(), city.upper()] for [[(country, city)]] in countries]
print(formatted)

#5.-
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list = [{'country': country.upper(), 'city': city.upper()} for [[(country, city)]] in countries]
print(dict_list)

#6.-
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for [[(first, last)]] in names]
print(full_names)

#7.-
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(slope(1, 2, 3, 4))  

y_intercept = lambda m, x, y: y - m * x
print(y_intercept(2, 3, 8)) 
