# Data Collection

## Dictionary

- Data are stored in key:value pairs
- It is an ordered collection. If using Python 3.6 or earlier it is unordered.
- It is mutable, i.e. values can be changed.
- It does not allow duplicates
- Syntax: variable_name = { "key" : value }

### Examples
```commandline
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
```
#### Built-in Methods
```
# Display keys only from student_1
print(student_1.keys())  # Output: dict_keys(['key', 'name', 'stream', 'completed_lessons', 'completed_lessons_names'])
print(type(student_1.keys()))  # Output: <class 'dict_keys'>

# Display values only from student_1
print(student_1.values())  # Output: dict_values(['values', 'Abhishek', 'DevOps', 4, ['lists', 'tuples', 'strings']])
print(type(student_1.values()))  # Output: <class 'dict_values'>
```

### Challenge Exercise

#### Task 1: Defining a dictionary
```
story1 = {
    "start": "DevOps is a set of practices that combines software development (Dev) and IT operations (Ops).",
    "middle": "It aims to shorten the SDLC and provide continuous delivery with high software quality.",
    "end": "DevOps is complementary with Agile software development."
}
```

#### Task 2: Printing the entire dictionary
```
print(story1) # Output: {'start': 'DevOps is a set of practices that combines software development (Dev) and IT operations (Ops).'
              # , 'middle': 'It aims to shorten the SDLC and provide continuous delivery with high software quality.', 
              # 'end': 'DevOps is complementary with Agile software development.'}
```

#### Task 3: Printing type of dictionary
```
print(type(story1))  # Output: <class 'dict'>
```

#### Task 4: Printing the keys
```
print(story1.keys())  # Output: dict_keys(['start', 'middle', 'end'])
```

#### Task 5: Printing only the values
```
print(story1.values())  # Output: dict_values(['DevOps is a set of practices that combines software development (Dev) and 
                        # IT operations (Ops).', 'It aims to shorten the SDLC and provide continuous delivery with high software 
                        # quality.', 'DevOps is complementary with Agile software development.'])
```

#### Task 6: Printing stories individually
```
print(story1["start"])   # Output: DevOps is a set of practices that combines software development (Dev) and IT operations (Ops).
print(story1["middle"])  # Output: It aims to shorten the SDLC and provide continuous delivery with high software quality.
print(story1["end"])     # Output: DevOps is complementary with Agile software development.
```

#### Task 7: Adding a new key:value pair.
```
story1["hero"] = "Spiderman"

# Printing the updated Dictionary value
print(story1["hero"])  # Output: Spiderman
```

