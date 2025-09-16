course_names = {}
student_grades = {}

section = input().strip()
while section != "EndOfInput":
    if section == "Courses":
        while True:
            line = input().strip()
            if line == "Students":
                break
            course_info = line.split("~")
            course_code = course_info[0]
            course_names[course_code] = course_info[1]

    elif section == "Students":
        while True:
            line = input().strip()
            if line == "Grades":
                break
            roll_number, full_name = line.split("~")
            student_grades[roll_number] = {"full_name": full_name, "grades": []}

    elif section == "Grades":
        while True:
            line = input().strip()
            if line == "EndOfInput":
                break
            course_code, semester, year, roll_number, grade = line.split("~")
            student_grades[roll_number]["grades"].append((course_code, grade))

    section = input().strip()

for roll_number, student_info in sorted(student_grades.items()):
    grades = student_info["grades"]
    total_grade_points = 0
    
