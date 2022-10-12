# Task 1: Defining a dictionary
story1 = {
    "start": "DevOps is a set of practices that combines software development (Dev) and IT operations (Ops).",
    "middle": "It aims to shorten the SDLC and provide continuous delivery with high software quality.",
    "end": "DevOps is complementary with Agile software development."
}

# Task 2: Printing the entire dictionary
print(story1)  # Output: {'start': 'DevOps is a set of practices that combines software development (Dev) and
# IT operations (Ops).', 'middle': 'It aims to shorten the SDLC and provide continuous delivery with high software
# quality.', 'end': 'DevOps is complementary with Agile software development.'}

# Task 3: Printing type of dictionary
print(type(story1))  # Output: <class 'dict'>

# Task 4: Printing the keys
print(story1.keys())  # Output: dict_keys(['start', 'middle', 'end'])

# Task 5: Printing only the values
print(story1.values())  # Output: dict_values(['DevOps is a set of practices that combines software development (Dev)
# and IT operations (Ops).', 'It aims to shorten the SDLC and provide continuous delivery with high software quality.',
# 'DevOps is complementary with Agile software development.'])


# Task 6: Printing stories individually
print(story1["start"])  # Output: DevOps is a set of practices that combines software development (Dev) and IT operations (Ops).
print(story1["middle"])  # Output: It aims to shorten the SDLC and provide continuous delivery with high software quality.
print(story1["end"])  # Output: DevOps is complementary with Agile software development.

# Task 7: Adding a new key:value pair.
story1["hero"] = "Spiderman"

# Printing the updated Dictionary value
print(story1["hero"])  # Output: Spiderman
