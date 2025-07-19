#1.-
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
print(random_user_id())

def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters per ID: "))
    num_ids = int(input("Enter number of IDs to generate: "))
    
    for _ in range(num_ids):
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))
        print(user_id)
print(user_id_gen_by_user())

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())