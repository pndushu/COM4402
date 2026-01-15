"""
nums = [3,  # 0
        6,  # 1
        9,  # 2
        12] # 3

print(nums[2:4])
"""
#colours list
"""
colours = ["red",#0
          "blue",#1
         "green"]#2
print(colours[0:1:2])
colours.append("yellow")
print(colours)
#choose a data structure + CRUD FUNCTIONS
"""
"""
def add_mark(marks, name, mark):
    marks[name] = mark


def get_mark(marks, name):
    return marks.get(name)


def update_mark(marks, name, new_mark):
    if name in marks:
        marks[name] = new_mark


def delete_mark(marks, name):
    if name in marks:
        del marks[name]
        """

# Classroom seating plan
"""
def create_row(names):
    return list(names)


def get_student_at(row, index):
    if 0 <= index < len(row):
        return row[index]
    return None


def swap_seats(row, index1, index2):
    if 0 <= index1 < len(row) and 0 <= index2 < len(row):
        row[index1], row[index2] = row[index2], row[index1]
        return True
    return False


def remove_student(row, name):
    if name in row:
        row.remove(name)
        return True
    return False
    """
#unique course codes
"""
# Using a set to store modules
modules = set()

def enrol_module(modules, code):
    modules.add(code)
    return modules

def is_enrolled(modules, code):
    return code in modules

def drop_module(modules, code):
    modules.discard(code)
    return modules

def count_modules(modules):
    return len(modules)


enrol_module(modules, "CS101")
enrol_module(modules, "MATH202")
print("Modules:", modules)
print("Enrolled in CS101?", is_enrolled(modules, "CS101"))
drop_module(modules, "CS101")
print("Modules after dropping CS101:", modules)
print("Number of modules:", count_modules(modules))
"""



