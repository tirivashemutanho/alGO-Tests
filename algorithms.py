

from time import time, perf_counter
def bubble_sort(students, key):
    swaps = 0
    iterations = 0
    start = perf_counter()
    for i in range(len(students)):
        for j in range(len(students) - i - 1):
            if students[j][key] > students[j + 1][key]:
                students[j], students[j + 1] = students[j + 1], students[j]
                swaps += 1
            iterations += 1
    end = perf_counter()
    elapsed = end - start
    return students

def selection_sort(students, key):
    swaps = 0
    iterations = 0
    start = perf_counter()
    for i in range(len(students)):
        min_index = i
        for j in range(i + 1, len(students)):
            if students[j][key] < students[min_index][key]:
                min_index = j
        if min_index != i:
            students[i], students[min_index] = students[min_index], students[i]
            swaps += 1
        iterations += 1
    end = perf_counter()
    elapsed = end - start
    return students


def insertion_sort(students, key):
    swaps = 0
    iterations = 0
    start = perf_counter()
    for i in range(len(students)):
        value = students[i]
        j = i
        while j > 0 and students[j - 1][key] > value[key]:
            students[j] = students[j - 1]
            swaps += 1
            j -= 1
        iterations += 1
        students[j] = value
    end = perf_counter()
    elapsed = end - start
    return students
def quick_sort(students, key):
    if len(students) <= 1:
        return students
    pivot = students[len(students) // 2][key]
    less = [x for x in students if x[key] < pivot]
    equal = [x for x in students if x[key] == pivot]
    greater = [x for x in students if x[key] > pivot]
    return quick_sort(less, key) + equal + quick_sort(greater, key)

def merge_sort(students, key):
    if len(students) <= 1:
        return students

    def merge(left, right, key):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][key] < right[j][key]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(students) // 2
    left = merge_sort(students[:mid], key)
    right = merge_sort(students[mid:], key)
    
    return merge(left, right, key)



def reverse_list(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    
    return lst








def linear_search(students, search_string):
    matching_students = []
    if search_string == "":
        matching_students = students  # Return all students if search string is empty

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


def binary_search(students, search_term):
    matching_students = []

    if search_term == "":
        matching_students = students  
    # Sort the students list
    students.sort(key=lambda x: x.get("firstname", "").lower())
    
    left = 0
    right = len(students) - 1

    while left <= right:
        mid = (left + right) // 2
        student = students[mid]

        if search_term.lower() in str(student.get("firstname", "")).lower() or \
           search_term.lower() in str(student.get("lastname", "")).lower() or \
           search_term.lower() in str(student.get("date_of_birth", "")).lower() or \
           search_term.lower() in str(student.get("gender", "")).lower() or \
           search_term.lower() in str(student.get("contact_number", "")).lower() or \
           search_term.lower() in str(student.get("email", "")).lower() or \
           search_term.lower() in str(student.get("address", "")).lower() or \
           search_term.lower() in str(student.get("program", "")).lower() or \
           search_term.lower() in str(student.get("gpa", "")).lower() or \
           search_term.lower() in str(student.get("accommodation", "")).lower():
            matching_students.append(student)

        if search_term.lower() < str(student.get("firstname", "")).lower():
            right = mid - 1
        else:
            left = mid + 1
            
    

    return matching_students

# code for ternary search

def ternary_search(students, search_term):
  matching_students = []

  if search_term == "":
    return students  # All students if search term is empty
  #sort the students lit
  students.sort(key=lambda x: x.get("firstname", "").lower())
  left = 0
  right = len(students) - 1

  while left <= right:
    left_third = left + (right - left) // 3
    right_third = right - (right - left) // 3

    left_student = students[left_third]
    right_student = students[right_third]

    if search_term.lower() in str(left_student.get("firstname", "")).lower():
      right = right_third
    elif search_term.lower() in str(right_student.get("firstname", "")).lower():
      left = left_third
    else:
      # Search term not found in middle thirds, check remaining portion
      potential_matches = students[left + 1:right]
      for student in potential_matches:
        if search_term.lower() in str(student.get("firstname", "")).lower() or \
           search_term.lower() in str(student.get("lastname", "")).lower() or \
           search_term.lower() in str(student.get("date_of_birth", "")).lower() or \
           search_term.lower() in str(student.get("gender", "")).lower() or \
           search_term.lower() in str(student.get("contact_number", "")).lower() or \
           search_term.lower() in str(student.get("email", "")).lower() or \
           search_term.lower() in str(student.get("address", "")).lower() or \
           search_term.lower() in str(student.get("program", "")).lower() or \
           search_term.lower() in str(student.get("gpa", "")).lower() or \
           search_term.lower() in str(student.get("accommodation", "")).lower():
          
           matching_students.append(student)
      break

  return matching_students

#hash table search

from collections import defaultdict

def hash_table_search(students, search_term):

  matching_students = []
  search_term = search_term.lower()

  # Create a hash table to store students by searchable fields (first and last name)
  hash_table = defaultdict(list)
  for student in students:
    first_name = student.get("firstname", "").lower()
    last_name = student.get("lastname", "").lower()
    hash_table[first_name].append(student)
    hash_table[last_name].append(student)

  # Check for matches in first and last name fields
  potential_matches = hash_table.get(search_term, []) + hash_table.get(search_term + " ", [])

  # Loop through potential matches and check other fields if necessary
  for student in potential_matches:
    if (search_term in str(student.get("firstname", "")).lower() or
        search_term in str(student.get("lastname", "")).lower() or
        search_term.lower() in str(student.get("date_of_birth", "")).lower() or \
        search_term.lower() in str(student.get("gender", "")).lower() or \
        search_term.lower() in str(student.get("contact_number", "")).lower() or \
        search_term.lower() in str(student.get("email", "")).lower() or \
        search_term.lower() in str(student.get("address", "")).lower() or \
        search_term.lower() in str(student.get("program", "")).lower() or \
        search_term.lower() in str(student.get("gpa", "")).lower() or \
        search_term.lower() in str(student.get("accommodation", "")).lower()):
        matching_students.append(student)

  return matching_students


