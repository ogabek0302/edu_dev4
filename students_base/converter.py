import json
import sqlite3

with open('students.json', encoding='utf-8') as f:
    students = json.load(f)
data = students

objects = json.loads(data)

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE people
             (name TEXT, age INT, city TEXT, nomer INT)''')
for obj in objects:
    id = obj['id']
    name = obj['name']
    group = obj['group']
    nomer = obj['nomer']
    c.execute("INSERT INTO people VALUES (?, ?, ?, ?)", (id, name, group, nomer))

conn.commit()
conn.close()
