def linear_search(students, search_string):
    matching_students = []

    if not search_string:  
        return students 

    if search_string == "student": 
        return students  

    for student in students:
       
        if search_string.lower() in str(student.get("firstname", "")).lower() or \
           search_string.lower() in str(student.get("lastname", "")).lower() or \
           search_string.lower() in str(student.get("date_of_birth", "")).lower() or \
           search_string.lower() in str(student.get("gender", "")).lower() or \
           search_string.lower() in str(student.get("contact_number", "")).lower() or \
           search_string.lower() in str(student.get("email", "")).lower() or \
           search_string.lower() in str(student.get("address", "")).lower() or \
           search_string.lower() in str(student.get("program", "")).lower() or \
           search_string.lower() in str(student.get("gpa", "")).lower() or \
           search_string.lower() in str(student.get("accommodation", "")).lower():
            matching_students.append(student)
            
    return matching_students

def binary_search(students, search_string):
    matching_students = []

    if not search_string:  
        return students  

    if search_string == "student":
        return students  

    
    students.sort(key=lambda x: x.get("firstname", "").lower())
    
    left = 0
    right = len(students) - 1

    while left <= right:
        mid = (left + right) // 2
        student = students[mid]

        if search_string.lower() in str(student.get("firstname", "")).lower() or \
           search_string.lower() in str(student.get("lastname", "")).lower() or \
           search_string.lower() in str(student.get("date_of_birth", "")).lower() or \
           search_string.lower() in str(student.get("gender", "")).lower() or \
           search_string.lower() in str(student.get("contact_number", "")).lower() or \
           search_string.lower() in str(student.get("email", "")).lower() or \
           search_string.lower() in str(student.get("address", "")).lower() or \
           search_string.lower() in str(student.get("program", "")).lower() or \
           search_string.lower() in str(student.get("gpa", "")).lower() or \
           search_string.lower() in str(student.get("accommodation", "")).lower():
            matching_students.append(student)

        if search_string.lower() < str(student.get("firstname", "")).lower():
            right = mid - 1
        else:
            left = mid + 1
            
    return matching_students


def hash_table_search(students, search_string):
    matching_students = []

    if not search_string:  
        return students  

    if search_string == "student":
        return students 

    hash_table = {}
    for student in students:
        key = hash(student['firstname']) % len(students)
        if key not in hash_table:
            hash_table[key] = []
        hash_table[key].append(student)

    # Search for the student
    search_key = hash(search_string) % len(students)
    if search_key in hash_table:
        for student in hash_table[search_key]:
            if (search_string.lower() in student['firstname'].lower() or
                search_string.lower() in student['lastname'].lower() or
                search_string.lower() in student['date_of_birth'].lower() or
                search_string.lower() in student['gender'].lower() or
                search_string.lower() in student['contact_number'].lower() or
                search_string.lower() in student['email'].lower() or
                search_string.lower() in student['address'].lower() or
                search_string.lower() in student['program'].lower() or
                search_string.lower() in str(student['gpa']).lower() or
                search_string.lower() in str(student['accommodation']).lower()):
                matching_students.append(student)

    return matching_students


def interpolation_search(students, search_string):
    matching_students = []

    if not search_string:  
        return students 

    if search_string == "student":
        return students  

    low = 0
    high = len(students) - 1

    while low <= high and search_string != "":
        pos = low + int((high - low) * ((ord(search_string[0].lower()) - ord('a')) / (ord('z') - ord('a'))))

        if pos < low or pos > high:
            break

        student = students[pos]

        if search_string.lower() in str(student.get("firstname", "")).lower() or \
           search_string.lower() in str(student.get("lastname", "")).lower() or \
           search_string.lower() in str(student.get("date_of_birth", "")).lower() or \
           search_string.lower() in str(student.get("gender", "")).lower() or \
           search_string.lower() in str(student.get("contact_number", "")).lower() or \
           search_string.lower() in str(student.get("email", "")).lower() or \
           search_string.lower() in str(student.get("address", "")).lower() or \
           search_string.lower() in str(student.get("program", "")).lower() or \
           search_string.lower() in str(student.get("gpa", "")).lower() or \
           search_string.lower() in str(student.get("accommodation", "")).lower():
            matching_students.append(student)
            break

        if search_string.lower() < student.get("firstname"):
            high = pos - 1
        else:
            low = pos + 1

    return matching_students


def ternary_search(students, search_string):


    matching_students = []

    if not search_string:  
        return students  

    if search_string == "student":
        return students  

    students.sort(key=lambda x: x.get("firstname", "").lower())
    left = 0
    right = len(students) - 1

    while left <= right:
        left_third = left + (right - left) // 3
        right_third = right - (right - left) // 3

        left_student = students[left_third]
        right_student = students[right_third]

        if search_string.lower() in str(left_student.get("firstname", "")).lower():
            right = right_third
        elif search_string.lower() in str(right_student.get("firstname", "")).lower():
            left = left_third
        else:
            
            potential_matches = students[left + 1:right]
            for student in potential_matches:
                if search_string.lower() in str(student.get("firstname", "")).lower() or \
                   search_string.lower() in str(student.get("lastname", "")).lower() or \
                   search_string.lower() in str(student.get("date_of_birth", "")).lower() or \
                   search_string.lower() in str(student.get("gender", "")).lower() or \
                   search_string.lower() in str(student.get("contact_number", "")).lower() or \
                   search_string.lower() in str(student.get("email", "")).lower() or \
                   search_string.lower() in str(student.get("address", "")).lower() or \
                   search_string.lower() in str(student.get("program", "")).lower() or \
                   search_string.lower() in str(student.get("gpa", "")).lower() or \
                   search_string.lower() in str(student.get("accommodation", "")).lower():
                    matching_students.append(student)
            break

    return matching_students


    if not search_string: 
            return students
    matching_students = []

    if search_string == "student":
        return students  
    students.sort(key=lambda x: x.get("firstname", "").lower())
    left = 0
    right = len(students) - 1

    while left <= right:
        left_third = left + (right - left) // 3
        right_third = right - (right - left) // 3

        left_student = students[left_third]
        right_student = students[right_third]

    if search_string.lower() in str(left_student.get("firstname", "")).lower():
      right = right_third
    elif search_string.lower() in str(right_student.get("firstname", "")).lower():
      left = left_third
    else:
     
        potential_matches = students[left + 1:right]
        for student in potential_matches:
            if search_string.lower() in str(student.get("firstname", "")).lower() or \
                search_string.lower() in str(student.get("lastname", "")).lower() or \
                search_string.lower() in str(student.get("date_of_birth", "")).lower() or \
                search_string.lower() in str(student.get("gender", "")).lower() or \
                search_string.lower() in str(student.get("contact_number", "")).lower() or \
                search_string.lower() in str(student.get("email", "")).lower() or \
                search_string.lower() in str(student.get("address", "")).lower() or \
                search_string.lower() in str(student.get("program", "")).lower() or \
                search_string.lower() in str(student.get("gpa", "")).lower() or \
                search_string.lower() in str(student.get("accommodation", "")).lower():
                
                matching_students.append(student)
            break

    return matching_students


def exponential_search(students, search_string):
    matching_students = []

    if not search_string:  
        return students  # Return all students if the search term is empty

    if search_string == "student":
        return students  # Return all students if the search term is "student"

    # Find the range for binary search
    bound = 1
    while bound < len(students) and search_string.lower() not in str(students[bound].get("firstname", "")).lower():
        bound *= 2

    left = bound // 2
    right = min(bound, len(students) - 1)

    # Perform binary search in the found range
    while left <= right:
        mid = (left + right) // 2
        student = students[mid]

        if search_string.lower() in str(student.get("firstname", "")).lower() or \
           search_string.lower() in str(student.get("lastname", "")).lower() or \
           search_string.lower() in str(student.get("date_of_birth", "")).lower() or \
           search_string.lower() in str(student.get("gender", "")).lower() or \
           search_string.lower() in str(student.get("contact_number", "")).lower() or \
           search_string.lower() in str(student.get("email", "")).lower() or \
           search_string.lower() in str(student.get("address", "")).lower() or \
           search_string.lower() in str(student.get("program", "")).lower() or \
           search_string.lower() in str(student.get("gpa", "")).lower() or \
           search_string.lower() in str(student.get("accommodation", "")).lower():
            matching_students.append(student)

        if search_string.lower() < str(student.get("firstname", "")).lower():
            right = mid - 1
        else:
            left = mid + 1
            
    return matching_students
