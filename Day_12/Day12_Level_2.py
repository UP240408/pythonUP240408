import random

#1.-
def list_of_hexa_colors(n):
    hex_colors = []
    for _ in range(n):
        hex_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        hex_colors.append(hex_color)
    return hex_colors

#2.-
def list_of_rgb_colors(n):
    rgb_colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f"rgb({r}, {g}, {b})")
    return rgb_colors

#3.-
def generate_colors(color_type, n):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type. Choose 'hexa' or 'rgb'."

print(generate_colors('hexa', 3))  
print(generate_colors('rgb', 2))   