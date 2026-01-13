# Calculator functions
"""""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("invalid choice")
"""

#fix the greeting
"""
def greet():
    message = "Hello from the function"
    return message

message = greet()
print(message)
"""

    #local vs global guess
"""
count = 0
def add_one(count):
    count = count + 1
    print("Inside:", count)
    return count
count= add_one(count)
print("Outside:", count)
"""
#complete the function
"""
def area_of_rectangle(width,height):
    area= width*height
    return area

w = float(input("Enter width: "))
h = float(input("Enter height: "))
print(f"area is {area_of_rectangle(w,h)}")
"""
#parameter vs global
"""
def calculate_tax(amount, rate):
    return amount * rate

tax = calculate_tax(100, 0.2)
print(tax)
"""
#Bug hunt:discount function
"""
def apply_discount(price):
    discount = 0
    if price > 100:
        discount = 10
    final_price = price - discount
    return final_price

p = float(input("Enter price: "))
result = apply_discount(p)
print("Final price:", result)
"""
#ATM Helper Functions
"""
def apply_discount(price):
    discount = 0
    if price > 100:
        discount = 10
    final_price = price - discount
    return final_price

p = float(input("Enter price: "))
result = apply_discount(p)
print("Final price:", result)
"""
# Scope Explanation in Comments
"""
def add_mark(total, mark):
    return total + mark

total = 0

mark1 = int(input("Enter mark 1: "))
total = add_mark(total, mark1)

mark2 = int(input("Enter mark 2: "))
total = add_mark(total, mark2)

print("Total:", total)
"""
#Rewrite Using Functions
"""
def get_user_details():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age


def print_message(name, age):
    if age >= 18:
        return f"Hello {name}, you are an adult."
    else:
        return f"Hello {name}, you are under 18."


# Main program
name, age = get_user_details()
message = print_message(name, age)
print(message)
"""
#(Medium) – Login + Scope
"""
def check_password(input_password):
    correct_password = "python123"
    if input_password == correct_password:
        return True
    else:
        return False


def login():
    password = input("Enter password: ")
    result = check_password(password)
    if result:
        return "Welcome"
    else:
        return "Access denied"


# Main program
message = login()
print(message)

#medium -refactor parking time calculator
"""
