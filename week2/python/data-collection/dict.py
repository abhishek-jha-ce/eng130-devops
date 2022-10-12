# Store student's data - name, course_name, progress, completed_lessons
student_1 = {
    "key": "values",
    "name": "Abhishek",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["lists", "tuples", "strings", "OOP"]
}

print(type(student_1))  # Output: <class 'dict'>
print(student_1["stream"])  # Output: DevOps
print(student_1["completed_lessons_names"])  # Output: ['lists', 'tuples', 'strings', 'OOP']
print(student_1["completed_lessons_names"][0])  # Output: lists
print(student_1["completed_lessons_names"][1])  # Output: tuples
print(student_1["completed_lessons_names"][2])  # Output: strings

# Changing Value
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])  # Output: 3

# Delete an item from the list
student_1["completed_lessons_names"].remove("OOP")  # Removes OOP if found, else shows an error
print(student_1["completed_lessons_names"])  # Output: ['lists', 'tuples', 'strings']

# Dict Built-in Methods
# Display keys only from student_1
print(student_1.keys())  # Output: dict_keys(['key', 'name', 'stream', 'completed_lessons', 'completed_lessons_names'])
print(type(student_1.keys()))  # Output: <class 'dict_keys'>

# Display values only from student_1
print(student_1.values())  # Output: dict_values(['values', 'Abhishek', 'DevOps', 4, ['lists', 'tuples', 'strings']])
print(type(student_1.values()))  # Output: <class 'dict_values'>
