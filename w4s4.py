"""
person = {
    "name": "Sam",
    "city": "London"
}

person["age"] = 20
person["city"] = "Bolton"
person["age"] = int(input("Enter age: "))
person["user"] = True

print(person)

for key, value in person.items():
    print(key, ":", value)
    """
from decorator import append

#courses
"""
courses = {
    "python": {
        "students": ["Ali", "Sara", "Tom", "Ali"],
        "max_size": 3
    },
    "datasci": {
        "students": ["Sara", "Imran"],
        "max_size": 2
    }
}

student_counts = {}

for course, info in courses.items():
    unique_students = set(info["students"])
    print(f"{course} students:", unique_students)

    if len(unique_students) > info["max_size"]:
        print("FULL")
    else:
        print("OK")

    for student in unique_students:
        if student not in student_counts:
            student_counts[student] = 0
        student_counts[student] += 1

print("\nStudent counts across courses:")
print(student_counts)
"""
#unique course codes
module  ={}
def enrol_module(modules, code):
 """Add a module code if not already present."""
 modules.add(code)
 return module
 # TODO
def is_enrolled(modules, code):
    for
 """Return True if the student is enrolled on this module."""
 # TODO
def drop_module(modules, code):
 """Remove a module if present."""
 # TODO
def count_modules(modules):
 """Return how many modules the student is taking."""

