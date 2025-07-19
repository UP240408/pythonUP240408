#1.-
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#2.-
def are_items_unique(lst):
    return len(lst) == len(set(lst))
#3.-
def are_items_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)
#4.-
import keyword

def is_valid_variable(var):
    return var.isidentifier() and not keyword.iskeyword(var)
#5.-

from collections import Counter
from countries_data import datos_de_paises

def most_spoken_languages(data, top_n=10):
    language_counter = Counter()
    for country in data:
        for lang in country["languages"]:
            language_counter[lang] += 1
    return language_counter.most_common(top_n)

def most_populated_countries(data, top_n=10):
    sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:top_n]]

