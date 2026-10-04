# Dictionary in Python
# A dictionary stores data in key-value pairs.
# - Keys must be unique
# - Values can be duplicate
# - It keeps insertion order
# - It can store different data types
# - It is mutable (can change after creation)

# Example 1: Create a dictionary
student = {
    "name": "Akash",
    "age": 21,
    "city": "Bangalore",
    "marks": [80, 90, 85]
}

print("Student dictionary:", student)
print("Type:", type(student))

# Example 2: Access values
print("Name:", student["name"])
print("Age:", student.get("age"))

# Example 3: Add a new key-value pair
student["course"] = "Python"
print("After adding course:", student)

# Example 4: Update an existing value
student["age"] = 22
print("After updating age:", student)

# Example 5: Remove a value
student.pop("city")
print("After removing city:", student)

# Example 6: Loop through dictionary
print("\nLooping through dictionary:")

for i in student:
    print(i, ":", student[i])
# Example 7: Nested dictionary
employee = {
    "name": "Riya",
    "skills": {
        "python": True,
        "java": False
    }
}
print("\nNested dictionary:", employee)
print("Python skill:", employee["skills"]["python"])

# Example 8: Useful dictionary methods
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Length:", len(student))
print("Copy:", student.copy())

# Summary
# Dictionary is useful when you want to store data by name instead of index.
# Example: phonebook, student records, config settings, etc.
