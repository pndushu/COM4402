#repeat a word
#word = input("Enter a word: ")
#n = int(input("Enter a number: "))

#for i in range(1, n + 1):
 #   print(f"{i}: {word}")
#sum of first numbers
#n = int(input("Enter an integer: "))

#total = 0
#for i in range(1, n + 1):
   # total += i

#print("The sum of numbers from 1 to", n, "is:", total)

#multiplication table
#x = int(input("Enter a number: "))

#for i in range(1, 11):
 #   print(f"{i} x {x} = {i * x}")

#count characters (non space)
#sentence = input("Enter a sentence: ")

#count = 0
#for char in sentence:
 #   if char != " ":
  #      count += 1

#print("Number of non-space characters:", count)

""""
find maximum mark
n = int(input("How many marks will you enter? "))

max_mark = None

for i in range(n):
    mark = int(input(f"Enter mark {i + 1}: "))
    if max_mark is None or mark > max_mark:
        max_mark = mark

print("The highest mark entered is:", max_mark)
"""
"""
# filter passing marks
n = int(input("How many marks will you enter? "))

pass_count = 0

for i in range(n):
    mark = int(input(f"Enter mark {i + 1}: "))
    if mark >= 40:
        print(mark)
        pass_count += 1

print("Number of students who passed:", pass_count)
"""
"""
#Reverse a String (Manual)
word = input("Enter a word: ")

reversed_word = ""
for char in word:
    reversed_word = char + reversed_word

print("Reversed word:", reversed_word)
"""
"""
#count specific letter in a list of names
n = int(input("How many names will you enter? "))

names = []
for i in range(n):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

letter = input("Enter a letter to search for: ").lower()

count = 0
for name in names:
    for char in name:
        if char == letter:
            print()


print("Number of names containing the letter:", count
"""
"""
#grade statistics
n = int(input("How many numbers will you enter? "))

numbers = []
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

for num in numbers:
    print("*" * num)
"""


