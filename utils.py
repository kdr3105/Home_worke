import json
def load_candidates_from_json(path='candidate.json'): # возвращает список всех кандидатов
    list_of_candidates = read_json_file(path)
    print_data = ''
    print_data += '<pre>\n'
    for i in list_of_candidates:
        print_data += f"Имя кандидата - {i['name']}\n"
        print_data += f"Позиция кандидата {i['position']}\n"
        print_data += f"Навыки через запятую {i['skills']}\n"
        print_data += f"=========================================================\n"
    print_data += '</pre>'
    return print_data
def get_candidate(candidate_id): # возвращает одного кандидата по его id
    list_of_candidates = read_json_file()
    print_candidat = ''
    exist_candidate = True
    for i in list_of_candidates:
        if i['id'] == candidate_id:
            print_candidat = f'<img src="{i["picture"]}"/>\n'
            print_candidat += f"</img>\n"
            print_candidat += f"<рге>\n"
            print_candidat += f"Имя кандидата - {i['name']}\n"
            print_candidat += f"Позиция кандидата {i['position']}\n"
            print_candidat += f"Навыки через запятую {i['skills']}\n"
            print_candidat += f"</рге>\n"
            exist_candidate = False
            break
    if exist_candidate:
        print_candidat += f"<рге>\n"
        print_candidat += f"Нет такого кандидата\n"
        print_candidat += f"</рге>\n"
    return print_candidat
def get_candidates_by_name(candidate_name): # возвращает кандидатов по имени
    list_of_candidates = read_json_file()
    name_data = '<pre>\n'
    exist_name = True
    for i in list_of_candidates:
        if str(candidate_name).lower() in str(i["name"]).lower().split():
            name_data += f"Имя кандидата - {i['name']}\n"
            name_data += f"Позиция кандидата {i['position']}\n"
            name_data += f"Навыки через запятую {i['skills']}\n"
            name_data += f"=========================================================\n"
            exist_name = False
    if exist_name:
        name_data += "Нет кандидатов с таким именем\n"
    name_data += '</pre>\n'
    return name_data
def get_candidates_by_skill(skill_name): # возвращает кандидатов по навыку
    list_of_candidates = read_json_file()
    skill_data = ''
    skill_data += '<pre>\n'
    exist_skils = True
    for i in list_of_candidates:
        if str(skill_name).lower() in str(i["skills"]).lower().split(', '):
            skill_data += f"Имя кандидата - {i['name']}\n"
            skill_data += f"Позиция кандидата {i['position']}\n"
            skill_data += f"Навыки через запятую {i['skills']}\n"
            skill_data += f"=========================================================\n"
            exist_skils = False
    if exist_skils:
        skill_data += "Нет кандидатов с таким навыком\n"
    skill_data += '</pre>\n'
    return skill_data
def read_json_file(path='candidate.json'):
    with open(path, 'r', ) as f:
        my_candidats = json.load(f)
    return  my_candidats


# print(load_candidates_from_json())
# print(get_candidate(5))
# print(get_candidates_by_skill('Python'))
# print(get_candidates_by_name('Torres'))