grade_points = {
    "A": 10,
    "AB": 9,
    "B": 8,
    "BC": 7,
    "C": 6,
    "CD": 5,
    "D": 4
}

import sys

students = {}
grades = {}

section = None

for line in sys.stdin:
    line = line.strip()
    if line == "EndOfInput":
        break
    if line in ["Courses", "Students", "Grades"]:
        section = line
        continue

    if section == "Students":
        roll, name = line.split("~")
        students[roll] = name
        grades[roll] = []   # initialize empty grade list

    elif section == "Grades":
        course, sem, year, roll, grade = line.split("~")
        if roll in grades:
            grades[roll].append(grade_points[grade])


for roll in sorted(students.keys()):
    g_list = grades[roll]
    if g_list:
        gpa = round(sum(g_list) / len(g_list), 2)
    else:
        gpa = 0
    print(f"{roll}~{students[roll]}~{gpa}")
