# Create dictionaries to store course information, student names, and grades
courses = {}
students = {}
grades = {}

# Read input
section = input()
while section != "EndOfInput":
    if section == "Courses":
        while True:
            course_info = input().split("~")
            if course_info[0] == "Students":
                break
            courses[course_info[0]] = course_info[1:]
    elif section == "Students":
        while True:
            student_info = input().split("~")
            if student_info[0] == "Grades":
                break
            students[student_info[0]] = student_info[1]
    elif section == "Grades":
        while True:
            grade_info = input().split("~")
            if grade_info[0] == "EndOfInput":
                break
            course_code = grade_info[0]
            semester = grade_info[1]
            year = grade_info[2]
            roll_number = grade_info[3]
            grade = grade_info[4]
            
            # Calculate grade points based on grade
            grade_points = {"A": 10, "AB": 9, "B": 8, "BC": 7, "C": 6, "CD": 5, "D": 4}
            grade_point = grade_points.get(grade, 0)
            
            # Store grades in the dictionary
            if roll_number in grades:
                grades[roll_number].append(grade_point)
            else:
                grades[roll_number] = [grade_point]
    section = input()

# Calculate and print the grade point average for each student
for roll_number, grade_list in sorted(grades.items()):
    full_name = students.get(roll_number, "")
    average_grade_point = round(sum(grade_list) / len(grade_list), 2) if grade_list else 0.0
    print(f"{roll_number}~{full_name}~{average_grade_point}")
