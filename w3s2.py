"""
start = int(input("Enter the starting number: "))

while start >= 1:
    print(start)
    start -= 1

print("Lift off!")





#sum until zero
total = 0

while True:
    num = int(input("Enter an integer (0 to stop): "))
    if num == 0:
        break
    total += num

print("Total sum:", total)



#pasword checker
correct_password = "python123"

while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Try again")


#guess the secret number
secret = 17

while True:
    guess = int(input("Guess the secret number: "))

    if guess == secret:
        print("Well done")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")



#menu loop-simple calculator
while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "0":
        print("Exiting the calculator.")
        break
    elif choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 + num2)
    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 - num2)
    else:
        print("Invalid choice, try again.")



# input validation:
while True:
    num = int(input("Enter a positive integer: "))
    if num > 0:
        print("You entered:", num)
        break
    else:
        print("Error! Please enter a positive integer.")





# average o0f marks until-1
total = 0
count = 0

while True:
    mark = int(input("Enter a mark (0-100) or -1 to stop: "))

    if mark == -1:
        break
    elif 0 <= mark <= 100:
        total += mark
        count += 1
    else:
        print("Invalid mark! Please enter a number between 0 and 100.")

if count > 0:
    average = total / count
    print("Number of marks entered:", count)
    print("Average mark:", average)
else:
    print("No marks were entered.")
""""""




"
#Limited login
correct_username = "user123"
correct_password = "pass123"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        attempts += 1
        print("Incorrect username or password.")
else:
    print("Account locked")
"""



"""
#bank balance simulator
balance = 100

while balance > 0:
    print("Current balance:", balance)
    withdrawal = float(input("Enter withdrawal amount (0 to stop): "))

    if withdrawal == 0:
        break
    elif withdrawal <= balance:
        balance -= withdrawal
        print("Withdrawal successful.")
    else:
        print("Insufficient funds.")

print("Final balance:", balance)





#text menu with do while style
last_name = None

while True:
    print("\nMenu:")
    print("1. Enter name")
    print("2. Show last name entered")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "0":
        print("Exiting menu.")
        break
    elif choice == "1":
        last_name = input("Enter a name: ")
        print("Name saved.")
    elif choice == "2":
        if last_name:
            print("Last name entered:", last_name)
        else:
            print("No name entered yet.")
    else:
        print("Invalid choice, try again.")
"""