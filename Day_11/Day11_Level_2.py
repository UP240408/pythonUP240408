#1.-
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    return f'The number of odds are {odds}.\nThe number of evens are {evens}.'

#2.-
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
#2.-
def is_empty(param):
    return param == '' or param == [] or param == {} or param is None
#3.-
#mean
def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0
#median
def calculate_median(lst):
    if not lst:
        return 0
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    else:
        return lst[mid]
from collections import Counter
#calculate_mode
def calculate_mode(lst):
    if not lst:
        return None
    freq = Counter(lst)
    max_freq = max(freq.values())
    mode = [k for k, v in freq.items() if v == max_freq]
    return mode if len(mode) > 1 else mode[0]
#calculate_range
def calculate_range(lst):
    return max(lst) - min(lst) if lst else 0
#calculate_variance
def calculate_variance(lst):
    if not lst:
        return 0
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)
import math
#calculate_std
def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))
