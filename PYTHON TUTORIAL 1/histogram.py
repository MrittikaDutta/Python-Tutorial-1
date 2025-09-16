def histogram(l):
    l1=[]
    d={0 for i in l}
    le=len(l)
    for i in l:
        d[i]=d[i]+1
    for i in d:
        l1.append((i,d))
    return l1
print(histogram([12,8,9,0,5,5,6,2,5]))

def histogram(l):
    # Create a dictionary to store the counts of each number
    count_dict = {}
    for num in l:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Create a list of pairs (number, count) from the dictionary
    pairs = [(num, count) for num, count in count_dict.items()]
    
    # Sort the list of pairs by count and then by number
    sorted_pairs = sorted(pairs, key=lambda x: (x[1], x[0]))
    
    return sorted_pairs
def transcript(coursedetails, studentdetails, grades):
    # Create dictionaries to store course details and student details for efficient lookup
    course_dict = {code: name for code, name in coursedetails}
    student_dict = {roll: name for roll, name in studentdetails}
    
    # Create a dictionary to store student grades
    student_grades = {}
    for roll, code, grade in grades:
        if roll not in student_grades:
            student_grades[roll] = []
        student_grades[roll].append((code, course_dict[code], grade))
    
    # Create the final consolidated grades list
    consolidated_grades = []
    for roll, name in sorted(studentdetails, key=lambda x: x[0]):
        if roll in student_grades:
            student_grades[roll].sort(key=lambda x: x[0])
            consolidated_grades.append((roll, name, student_grades[roll]))
    
    return consolidated_grades