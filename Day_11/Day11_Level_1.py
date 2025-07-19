import math

# 1.-
def add_two_numbers(a, b):
    return a + b

# 2.-
def area_of_circle(r):
    return math.pi * r * r

# 3.-
def add_all_nums(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args)
    return "All inputs must be numbers."

# 4.-
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 5.-
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    else:
        return "Invalid month name."

# 6.-
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Undefined slope (vertical line)"
    return (y2 - y1) / (x2 - x1)

# 7.-
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solution"
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)

# 8.-
def print_list(lst):
    for item in lst:
        print(item)

# 9.-
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# 10.-
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# 11.-
def add_item(lst, item):
    return lst + [item]

# 12.-
def remove_item(lst, item):
    return [x for x in lst if x != item]

# 13.-
def sum_of_numbers(n):
    return sum(range(n+1))

# 14.-
def sum_of_odds(n):
    return sum(x for x in range(n+1) if x % 2 != 0)

# 15.-
def sum_of_even(n):
    return sum(x for x in range(n+1) if x % 2 == 0)
