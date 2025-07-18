#1.-
from countries import countries

land_countries = [country for country in countries if 'land' in country]
print(land_countries)
print("----------------------------------")
#2.-
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)
print("----------------------------------")
#3.1.-
from countries_data import datos_de_paises

all_languages = set()
for country in datos_de_paises:
    for language in country['languages']:
        all_languages.add(language)

print(f"Total number of unique languages: {len(all_languages)}")
print("----------------------------------")
#3.2.-
from collections import Counter

language_counter = Counter()
for country in datos_de_paises:
    for language in country['languages']:
        language_counter[language] += 1

most_spoken = language_counter.most_common(10)
print(most_spoken)
print("-----------------------------------")
#3.3.-
most_populated = sorted(datos_de_paises, key=lambda x: x['population'], reverse=True)[:10]
for country in most_populated:
    print(f"{country['name']}: {country['population']}")
    print()
