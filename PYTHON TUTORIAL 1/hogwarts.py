
grade_points = {'A': 10, 'AB': 9, 'B': 8, 'BC': 7, 'C': 6, 'CD': 5, 'D': 4}
students = {}
section = input().strip()
while section != "EndOfInput":
    if section == "Courses":
        courses = {}
        while True:
            line = input().strip()
            if line == "Students":
                break
            course_code, course_name, _, _, _ = line.split('~')
            courses[course_code] = course_name
    elif section == "Students":
        while True:
            line = input().strip()
            if line == "Grades":
                break
            roll_number, full_name = line.split('~')
            students[roll_number] = {'full_name': full_name, 'grades': {}}
    elif section == "Grades":
        while True:
            line = input().strip()
            if line == "EndOfInput":
                break
            course_code, _, _, roll_number, grade = line.split('~')
            students[roll_number]['grades'][course_code] = grade_points[grade]
    
    section = input().strip()

for roll_number, student_info in sorted(students.items()):
    full_name = student_info['full_name']
    grades = student_info['grades']
    if grades:
        gpa = round(sum(grades.values()) / len(grades), 2)
    else:
        gpa = 0.0
    print(f"{roll_number}~{full_name}~{gpa}")
