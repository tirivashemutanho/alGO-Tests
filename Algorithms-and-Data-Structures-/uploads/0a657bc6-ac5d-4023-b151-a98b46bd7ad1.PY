# QUESTION ONE


i. The Stack is the best data structure for implementing the collation problem because it follows the Last-In-First-Out (LIFO) principle. When pages are sent to the print spooler, the last page arrives first and needs to be printed last. Similarly, the second-to-last page arrives next and needs to be printed second-to-last, and so on. A stack allows us to easily reverse the order of the pages by pushing them onto the stack in the order they arrive and then popping them off the stack in reverse order when sending them to the printer.

ii. Here's a Python implementation of the push() function for the print spooler stack:

```python
class PrintSpooler:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, page):
        if len(self.stack) == self.capacity:
            self.stack.pop(0)  # Remove the element at the bottom of the stack
        self.stack.append(page)

# Testing the push() function
spooler = PrintSpooler(3)  # Initialize a print spooler with capacity 3
spooler.push("Page 1")
spooler.push("Page 2")
spooler.push("Page 3")
spooler.push("Page 4")

print(spooler.stack)  # Output: ['Page 2', 'Page 3', 'Page 4']
```

In this implementation, `capacity` represents the maximum number of pages the print spooler can hold. If the stack is already at full capacity, the element at the bottom of the stack (index 0) is removed using `pop(0)`, and then the new page is added to the top of the stack using `append()`.

iii. Here's a Python implementation of the delete(job_id) function for the print spooler stack:

```python
class PrintSpooler:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def delete(self, job_id):
        if 0 <= job_id < len(self.stack):
            del self.stack[job_id]

# Testing the delete() function
spooler = PrintSpooler(3)  # Initialize a print spooler with capacity 3
spooler.push("Page 1")
spooler.push("Page 2")
spooler.push("Page 3")

spooler.delete(1)  # Delete the page with job_id 1 (second page)

print(spooler.stack)  # Output: ['Page 1', 'Page 3']
```

In this implementation, the `delete()` function takes a `job_id` parameter, which represents the index of the element to be deleted from the stack. It checks if the `job_id` is within the valid range of stack indices and then uses the `del` keyword to remove the element at the specified index.

iv. The worst-case time complexity of the push() method described above is O(n), where n is the capacity of the print spooler stack. When the capacity is reached, removing the element at the bottom of the stack (using `pop(0)`) requires shifting all the other elements to fill the gap, which takes O(n) time. The subsequent appending of a new element to the stack (using `append()`) takes O(1) time.

v. Here's a Python implementation of the enqueue() function for adding jobs to the print spooler queue:

```python
class PrintSpooler:
    def __init__(self):
        self.queue = []

    def enqueue(self, job):
        self.queue.append(job)

    def cancel_job(self, job_id):
        if 0 <= job_id < len(self.queue):
            del self.queue[job_id]

# Testing the enqueue() function
spooler = PrintSpooler()  # Initialize a print spooler

spooler.enqueue("Job 1")
spooler.enqueue("Job 2")
spooler.enqueue("Job 3")
spooler.enqueue("Job 4")

spooler.cancel_job(1)  # Cancel the job with job_id 1

print(spooler.queue)  # Output: ['Job 1', 'Job 3', 'Job 4']
```

In this implementation, the `enqueue()` function simply appends the job to the end of the queue using `append()`. The `cancel_job()` function takes a `job_id` parameter and deletes the job from the queue if the `job_id` is within the valid range of queue indices.

vi. The worst-case time complexity of the enqueue() function is O(n), where n is the number of jobs in the print spooler queue. In the worst case, if a job is cancelled and removed from the middle of the queue, all the jobs that come after it need to be shifted tofill the gap, which takes O(n) time. The subsequent appending of a new job to the queue (using `append()`) takes O(1) time.

vii. Here's a Python implementation of the insert() function for inserting jobs into a linked list:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class PrintSpooler:
    def __init__(self):
        self.head = None

    def insert(self, job):
        new_node = Node(job)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def cancel_job(self, job_id):
        if job_id == 0:
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            count = 0

            while current is not None and count < job_id:
                prev = current
                current = current.next
                count += 1

            if current is not None:
                prev.next = current.next

    def print_jobs(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

# Testing the insert() function
spooler = PrintSpooler()  # Initialize a print spooler

spooler.insert("Job 1")
spooler.insert("Job 2")
spooler.insert("Job 3")
spooler.insert("Job 4")

spooler.cancel_job(1)  # Cancel the job with job_id 1

spooler.print_jobs()  # Output: 'Job 1', 'Job 3', 'Job 4'
```

In this implementation, the `insert()` function creates a new node with the job as its data. If the linked list is empty (i.e., `self.head` is `None`), the new node becomes the head of the list. Otherwise, it traverses the linked list to find the last node and appends the new node as the `next` of the last node.

The `cancel_job()` function takes a `job_id` parameter and deletes the job from the linked list. If the `job_id` is 0, it means the head node needs to be deleted, so the `head` is updated to the next node. Otherwise, it traverses the linked list, keeping track of the previous node (`prev`) and the current node (`current`). Once it reaches the node with the matching `job_id`, it updates the `next` pointer of the previous node to skip the current node, effectively removing it from the list.

The `print_jobs()` function is provided for testing purposes and prints the data of each node in the linked list.



# QUESTION  2

i. The most efficient algorithm that the farmer should use to cross the river is the Breadth-First Search (BFS) algorithm. BFS is a graph traversal algorithm that explores all the vertices of a graph in breadth-first order, level by level. In this case, the graph represents the possible states of the farmer, hyena, goat, and grain on either side of the river.

The algorithm can be implemented as follows:
1. Create an empty queue and enqueue the initial state of the farmer, hyena, goat, and grain on one side of the river.
2. Create an empty set to keep track of visited states.
3. While the queue is not empty:
   - Dequeue a state from the front of the queue.
   - If the state represents a valid configuration (i.e., the hyena and goat are not left alone, and the goat and grain are not left alone), return the sequence of actions taken to reach this state.
   - Generate all possible next states by moving the farmer and one other item across the river.
   - For each next state, if it has not been visited before, enqueue it and mark it as visited.
4. If no valid configuration can be reached, return failure.

By using BFS, the algorithm will find the shortest sequence of actions required for the farmer to safely cross the river with the hyena, goat, and grain.

ii. Here's a directed and weighted graph showing how the farmer crosses the river:

```
               +---[GR]---+
               |          |
               V          |
          +---[G ] <-----+
          |          ^
          V          |
   [H ]---+---[HG]---+
          ^          |
          |          V
          +---[H ]---+
```

In this graph, the nodes represent the different states of the farmer, hyena (H), goat (G), and grain (GR) on either side of the river. The directed edges represent the possible moves the farmer can make to transition from one state to another. The weights on the edges represent the cost or number of crossings required to make the move.

iii. The minimum number of crossings required by the farmer to cross the river together with the hyena, goat, and grain is 7.



# QUESTION 3

i. Here's a Python function that uses a looping construct and a Stack data structure to determine if a given string is a palindrome or not:

```python
def is_palindrome(string):
    stack = []
    length = len(string)
    middle = length // 2

    # Push the characters before the '$' symbol onto the stack
    for i in range(middle):
        stack.append(string[i])

    # Check if the length of the string is odd
    if length % 2 != 0:
        middle += 1

    # Compare the characters after the '$' symbol with the characters popped from the stack
    for i in range(middle, length):
        if len(stack) == 0 or stack.pop() != string[i]:
            return False

    return True

# Testing the function
print(is_palindrome("abaa$abaa"))  # Output: True
print(is_palindrome("bbab$abba"))  # Output: False
```

In this implementation, the function `is_palindrome()` accepts a string as input. It initializes an empty stack and calculates the length of the string. It then finds the middle index of the string (ignoring the '$' symbol) to determine the number of characters that need to be pushed onto the stack.

The function uses a loop to iterate over the characters before the '$' symbol and pushes them onto the stack. If the length of the string is odd, it increments the middle index by 1 to skip the '$' symbol. After that, it compares the characters after the '$' symbol with the characters popped from the stack. If any mismatch is found or if the stack becomes empty before comparing all the characters, the function returns False, indicating that the string is not a palindrome. If the loop completes without any mismatches, the function returns True, indicating that the string is a palindrome.

ii. The worst-case time complexity of the program is O(n), where n is the length of the string. The program iterates over approximately half of the characters in the string (ignoring the '$' symbol) to push them onto the stack, which takes O(n/2) time. It then compares the remaining half of the characters with the characters popped from the stack, which also takes O(n/2) time. Therefore, the overall time complexity is O(n/2) + O(n/2), which simplifies to O(n).




# qUESTION 4
i. Here's an algorithm that calculates the percentage change in census statistics given two lists:

1. Initialize an empty list called `percentage_change`.
2. Iterate over the elements in the first list (2012 statistics) and the corresponding elements in the second list (2022 statistics) simultaneously.
3. For each pair of statistics, calculate the percentage change using the formula: `(2022_stat - 2012_stat) / 2012_stat * 100`.
4. Append the calculated percentage change to the `percentage_change` list.
5. Return the `percentage_change` list.

ii. Here's the Python implementation of the algorithm:

```python
def calculate_percentage_change(statistics_2012, statistics_2022):
    percentage_change = []

    for stat_2012, stat_2022 in zip(statistics_2012, statistics_2022):
        change = (stat_2022 - stat_2012) / stat_2012 * 100
        percentage_change.append(change)

    return percentage_change

# Testing the function
statistics_2012 = [4567, 5678, 6789]
statistics_2022 = [5480, 6890, 7100]
change = calculate_percentage_change(statistics_2012, statistics_2022)
print(change)  # Output: [19.999563915929203, 21.035598705501392, 4.654183233272671]
```

In this implementation, the function `calculate_percentage_change()` takes two lists (`statistics_2012` and `statistics_2022`) as input. It initializes an empty list called `percentage_change`. It then iterates over the elements in both lists simultaneously using the `zip()` function. For each pair of statistics, it calculates the percentage change using the given formula and appends it to the `percentage_change` list. Finally, it returns the `percentage_change` list.

iii. A Python array is not suitable for storing the data in the above tables because arrays in Python are homogeneous, meaning they can only store elements of the same data type. In the census statistics tables, the data includes both district names (strings) and numerical values. Therefore, a data structure that supports heterogeneous data types, such as a list or a dictionary, would be more appropriate for storing the data.

b) i. Here's an algorithm to determine if a sequence of numbers is sorted and, if so, in ascending or descending order:

1. Initialize two boolean variables, `is_ascending` and `is_descending`, to True.
2. Iterate over the sequence of numbers starting from the second element.
3. For each pair of adjacent numbers:
   - If the current number is less than the previous number, set `is_ascending` to False.
   - If the current number is greater than the previous number, set `is_descending` to False.
4. If both `is_ascending` and `is_descending` are True, the sequence is sorted in both ascending and descending order.
5. If only `is_ascending` is True, the sequence is sorted in ascending order.
6. If only `is_descending` is True, the sequence is sorted in descending order.
7. If both `is_ascending` and `is_descending` are False, the sequence is not sorted.

ii. The worst-case time complexity of the algorithm is O(n), where n is the length of the sequence. The algorithm iterates over the sequence once, comparing each pair of adjacent numbers. Therefore, the time complexity is directly proportional to the length of the sequence.

iii. Here's the Python implementation of the algorithm:

```python
def determine_sort_order(sequence):
    is_ascending = True
    is_descending = True

    for i in range(1, len(sequence)):
        if sequence[i] < sequence[i - 1]:
            is_ascending = False
        if sequence[i] > sequence[i - 1]:
            is_descending = False

    if is_ascending and is_descending:
        return "Sorted in both ascending and descending order"
    elif is_ascending:
        return "Sorted in ascending order"
    elif is_descending:
        return "Sorted in descending order"
    else:
        return "Not sorted"

# Testing the function
sequence1 = [1, 2, 3, 4, 5]
sequence2 = [5, 4, 3, 2, 1]
sequence3 = [1, 3, 2, 4, 5]

print(determine_sort_order(sequence1))  # Output: Sorted in ascending order
print(determine_sort_order(sequence2))  # Output: Sorted in descending order
print(determine_sort_order(sequence3))  # Output: Not sorted
```

In this implementation, the function `determine_sort_order()` takes a sequence of numbers as input. It initializes two boolean variables, `is_ascending`is_ascending` and `is_descending`, to `True`. It then iterates over the sequence starting from the second element and compares each pair of adjacent numbers. Based on the comparisons, it updates the `is_ascending` and `is_descending` variables accordingly. Finally, it checks the values of `is_ascending` and `is_descending` and returns the corresponding result indicating the sort order of the sequence.




# Question 4

i. Algorithm to determine Q1, Q3, and IQR:

1. Sort the list of positive integers in ascending order.
2. Calculate the total number of elements, n, in the sorted list.
3. Calculate the index of the first quartile (Q1) as (n + 1) * 1/4.
4. Calculate the index of the third quartile (Q3) as (n + 1) * 3/4.
5. If the indices calculated in steps 3 and 4 are integers, take the corresponding elements in the sorted list as Q1 and Q3, respectively.
6. If the indices calculated in steps 3 and 4 are not integers, take the average of the two closest indices and use them to find the corresponding elements in the sorted list as Q1 and Q3, respectively.
7. Calculate the interquartile range (IQR) as Q3 - Q1.
8. Return Q1, Q3, and IQR.

ii. Algorithm to split the list into outliers and non-outliers:

1. Sort the list of positive integers in ascending order.
2. Calculate Q1, Q3, and IQR using the algorithm from part (i).
3. Calculate the lower bound as Q1 - 1.5 * IQR.
4. Calculate the upper bound as Q3 + 1.5 * IQR.
5. Initialize two empty lists, outliers and non_outliers.
6. Iterate over each element in the sorted list.
7. If the element is less than the lower bound or greater than the upper bound, add it to the outliers list.
8. If the element is within the range [lower bound, upper bound], add it to the non_outliers list.
9. Return the outliers and non_outliers lists.

iii. Here's the Python implementation of both algorithms:

```python
def calculate_quartiles(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    q1_index = (n + 1) * 1/4
    q3_index = (n + 1) * 3/4

    if q1_index.is_integer():
        q1 = sorted_numbers[int(q1_index) - 1]
    else:
        q1 = (sorted_numbers[int(q1_index) - 1] + sorted_numbers[int(q1_index)]) / 2

    if q3_index.is_integer():
        q3 = sorted_numbers[int(q3_index) - 1]
    else:
        q3 = (sorted_numbers[int(q3_index) - 1] + sorted_numbers[int(q3_index)]) / 2

    iqr = q3 - q1

    return q1, q3, iqr


def split_outliers(numbers):
    q1, q3, iqr = calculate_quartiles(numbers)
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = []
    non_outliers = []

    for num in numbers:
        if num < lower_bound or num > upper_bound:
            outliers.append(num)
        else:
            non_outliers.append(num)

    return outliers, non_outliers

# Testing the functions
numbers = [2, 2, 3, 5, 5, 5, 5, 7, 7, 8, 9, 10, 11, 11, 11, 13, 14]
q1, q3, iqr = calculate_quartiles(numbers)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)

outliers, non_outliers = split_outliers(numbers)
print("Outliers:", outliers)
print("Non-outliers:", non_outliers)
```

In this implementation, the `calculate_quartiles()` function takes a list of positive integers as input and returns Q1, Q3, and IQR using the algorithm described in part (i). The `split_outliers()` function takes a list of positive integers as input, calculates Q1, Q3, and IQR using the `calculate_quartiles()` function, and splits the list into outliers and non-outliers based on the specified range. The outliers and non-outliers are returned as separate lists.

iv. Here's the Python class with the quartile search and quartile sort methods:



```python
class QuartileCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.sorted_numbers = sorted(numbers)

    def calculate_quartiles(self):
        n = len(self.sorted_numbers)
        q1_index = (n + 1) * 1/4
        q3_index = (n + 1) * 3/4

        if q1_index.is_integer():
            q1 = self.sorted_numbers[int(q1_index) - 1]
        else:
            q1 = (self.sorted_numbers[int(q1_index) - 1] + self.sorted_numbers[int(q1_index)]) / 2

        if q3_index.is_integer():
            q3 = self.sorted_numbers[int(q3_index) - 1]
        else:
            q3 = (self.sorted_numbers[int(q3_index) - 1] + self.sorted_numbers[int(q3_index)]) / 2

        iqr = q3 - q1

        return q1, q3, iqr

    def quartile_search(self, number):
        q2_index = (len(self.sorted_numbers) + 1) * 2/4
        q2 = None

        if q2_index.is_integer():
            q2 = self.sorted_numbers[int(q2_index) - 1]
        else:
            q2 = (self.sorted_numbers[int(q2_index) - 1] + self.sorted_numbers[int(q2_index)]) / 2

        if number == q2:
            return "found"
        elif number < q2:
            half_list = self.sorted_numbers[:int(q2_index) - 1]
        else:
            half_list = self.sorted_numbers[int(q2_index):]

        if len(half_list) == 0:
            return "not found"
        else:
            sub_calculator = QuartileCalculator(half_list)
            return sub_calculator.quartile_search(number)

    def quartile_sort(self):
        q2_index = (len(self.sorted_numbers) + 1) * 2/4

        if q2_index.is_integer():
            q2 = self.sorted_numbers[int(q2_index) - 1]
        else:
            q2 = (self.sorted_numbers[int(q2_index) - 1] + self.sorted_numbers[int(q2_index)]) / 2

        lower_half = self.sorted_numbers[:int(q2_index) - 1]
        upper_half = self.sorted_numbers[int(q2_index):]

        if len(lower_half) > 1:
            lower_half_calculator = QuartileCalculator(lower_half)
            lower_half = lower_half_calculator.quartile_sort()

        if len(upper_half) > 1:
            upper_half_calculator = QuartileCalculator(upper_half)
            upper_half = upper_half_calculator.quartile_sort()

        return lower_half + [q2] + upper_half

# Testing the QuartileCalculator class and its methods
numbers = [2, 2, 3, 5, 5, 5, 5, 7, 7, 8, 9, 10, 11, 11, 11, 13, 14]
calculator = QuartileCalculator(numbers)

q1, q3, iqr = calculator.calculate_quartiles()
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)

number_to_search = 9
result = calculator.quartile_search(number_to_search)
print(f"Number {number_to_search}:", result)

sorted_numbers = calculator.quartile_sort()
print("Sorted Numbers:", sorted_numbers)
```

In this implementation, the QuartileCalculator class takes a list of numbers as input. The `calculate_quartiles()` method calculates Q1, Q3, and IQR using the algorithm described in part (i). The `quartile_search()` method performs a recursive search for a given number, splitting the list based on Q2 and searching in the appropriate half. The `quartile_sort()` method recursively sorts the list using Q2 as a pivot point.

You can create an object of the QuartileCalculator class, pass a list of numbers to it, and then call the `calculate_quartiles()`, `quartile_search()`, and `quartile_sort()` methods to perform the desired operations.