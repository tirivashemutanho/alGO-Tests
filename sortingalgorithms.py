from time import perf_counter


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


def heap_sort(students, key):
  n = len(students)
  for i in range(n // 2 - 1, -1, -1):
    heapify(students, n, i, key)
    
  for i in range(n - 1, 0, -1):
    students[i], students[0] = students[0], students[i]
    heapify(students, i, 0, key)
    
  return students

def heapify(students, n, i, key):
  largest = i
  l = 2 *i + 1
  r = 2 * i + 2
  
  if l< n and students[l][key] > students[largest][key]:
    largest = l
    
  if r< n and students[r][key] > students[largest][key]:
    largest = r
    
  if largest != i:
    students[i], students[largest] = students[largest], students[i]
    heapify(students, n, largest, key)
    


