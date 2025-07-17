person = {
    'first_name': 'Andres',
    'last_name': 'Chairez',
    'age': 18,
    'country': 'Mexico',
    'is_marred': True,
    'skills': ['JavaScript','React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Villas',
        'zipcode': '20286'
    }
}

# Comprobar si existe skills
if 'skills' in person:
    skills = person['skills']
    
    #  Print la skill de el medio
    mid_index = len(skills) // 2
    print("Middle skill:", skills[mid_index])
    
    #Comprobar si python esta en skills
    has_python = 'Python' in skills
    print("Tiene experiencia con python:", has_python)

    # Determinar Skills
    skill_set = set(skills)
    if skill_set == {'JavaScript', 'React'}:
        print('El es un front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skill_set):
        print('El es un backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skill_set):
        print('El es un fullstack developer')
    else:
        print('Unknown title')

# Comprobar estado civil y pais
if person.get('is_marred') and person.get('country') == 'Mexico':
    full_name = person['first_name'] + ' ' + person['last_name']
    print(f"{full_name} vive en Mexico. El  esta casado.")