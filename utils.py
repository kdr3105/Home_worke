import json
def load_candidates_from_json(path='candidate.json'): # возвращает список всех кандидатов
    list_of_candidates = read_json_file(path)
    print_data = []
    for i in list_of_candidates:
        stroka_data = []
        stroka_data.append(i['id'])
        stroka_data.append(i['name'])
        print_data.append(stroka_data)
    return print_data
def get_candidate(candidate_id): # возвращает одного кандидата по его id
    list_of_candidates = read_json_file()
    print_candidat = {}
    exist_candidate = True
    for i in list_of_candidates:
        if i['id'] == int(candidate_id):
            print_candidat['imegis'] = i["picture"]
            print_candidat['name'] = i['name']
            print_candidat['posiion'] = i['position']
            print_candidat['skilss'] = i['skills']
            exist_candidate = False
            break
    if exist_candidate:
        print_candidat['imegis'] = "Нет такого"
        print_candidat['name'] = "Нет такого"
        print_candidat['posiion'] = "Нет такого"
        print_candidat['skilss'] = "Нет такого"
    return print_candidat
def get_candidates_by_name(candidate_name): # возвращает кандидатов по имени
    list_of_candidates = read_json_file()
    name_data = []
    exist_name = True
    for i in list_of_candidates:
        if str(candidate_name).lower() in str(i["name"]).lower().split():
            stroka_data = []
            stroka_data.append(i['id'])
            stroka_data.append(i['name'])
            name_data.append(stroka_data)
            exist_name = False
    if exist_name:
        stroka_data = []
        stroka_data.append('id')
        stroka_data.append('name')
        name_data.append(stroka_data)
    return name_data
def get_candidates_by_skill(skill_name): # возвращает кандидатов по навыку
    list_of_candidates = read_json_file()
    skill_data = []
    exist_skils = True
    print(skill_name)
    for i in list_of_candidates:
        if str(skill_name).lower() in str(i["skills"]).lower().split(', '):
            stroka_data = []
            stroka_data.append(i['id'])
            stroka_data.append(i['name'])
            skill_data.append(stroka_data)
            exist_skils = False
    if exist_skils:
        stroka_data.append('id')
        stroka_data.append('name')
        skill_data.append(stroka_data)
    return skill_data
def read_json_file(path='candidate.json'):
    with open(path, 'r', ) as f:
        my_candidats = json.load(f)
    return  my_candidats


# print(load_candidates_from_json())
# print(get_candidate(5))
# print(get_candidates_by_skill('Python'))
# print(get_candidates_by_name('Torres'))