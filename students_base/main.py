import json
import random

GROUPS = ['Fullstack Python', 'Fullstack Javasqript', 'C#', 'Suniy intelect', 'Front end', 'Data science']

NUM_STUDENTS = 150

students = []

with open('all_names.json', encoding='utf-8') as f:
    names = json.load(f)

for i in range(1, NUM_STUDENTS + 1):
    student = {
        'id': i,
        'name': random.choice(names),
        'group': random.choice(GROUPS),
        'nomer': '+' + str(9989) + str(random.randint(10000000, 99999999))
    }
    students.append(student)


with open('students.json', 'w', encoding="utf-8") as outfile:
    json.dump(students, outfile, indent = 6, ensure_ascii=False)

print(f'Saved {NUM_STUDENTS} students to students.json')
