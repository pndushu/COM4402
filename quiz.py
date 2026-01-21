
# QUIZ PROGRAM
def calculate_score(user_answers, correct_answers):
    score = 0
    for i in range(len(correct_answers)):
        if user_answers[i].upper() == correct_answers[i].upper():
            score += 1
    return score

correct_answers = ("D", "A", "D", "A", "A")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful. Proceeding...")
else:
    print("Login failed. Program terminated.")
    exit()

print("Answer the following questions with the appropriate answers: A, B, C, D")

questions = [
    "Which one of the following lives under water:",
    "The best gospel artist in Zimbabwe?:",
    "What is the capital city of Zimbabwe?:",
    "Who was the first black president of Zimbabwe?:",
    "What is best used for large scale irrigation?:"
]

options = [
    ("A. DOG", "B. CAT", "C. ZEBRA", "D. FISH"),
    ("A. Charamba", "B. Manyeruke", "C. Zhakata", "D. Mhere"),
    ("A. Bindura", "B. Chegutu", "C. Chinhoyi", "D. Harare"),
    ("A. Robert", "B. Cannon", "C. Phillimon", "D. Joshua"),
    ("A. Pivot", "B. Drip", "C. Floods", "D. Sprinkler")
]

answers = ("D", "A", "D", "A", "A")

guesses = []
score = 0

# ASK QUESTIONS USING INDEX LOOP
for i in range(len(questions)):
    print("----------------")
    print(questions[i])

    # Loop through options
    for opt in options[i]:
        print(opt)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        print(f"The correct answer is: {answers[i]}")

# RESULTS SECTION
print("__________________________________________________")
print("                     RESULTS                      ")
print("__________________________________________________")

# Print answers
print("Answers: ", end="")
for ans in answers:
    print(ans, end=" ")
print()

# Print guesses
print("Guesses: ", end="")
for g in guesses:
    print(g, end=" ")
print()

percentage = int((score / len(questions)) * 100)
print(f"Your score in percentage is: {percentage}%")