# QUIZ PROGRAM
# QUIZ DATA AS LIST OF DICTIONARIES
quiz = [
    {
        "question": "Which one of the following lives under water:",
        "options": ["A. DOG", "B. CAT", "C. ZEBRA", "D. FISH"],
        "answer": "D"
    },
    {
        "question": "The best gospel artist in Zimbabwe?:",
        "options": ["A. Charamba", "B. Manyeruke", "C. Zhakata", "D. Mhere"],
        "answer": "A"
    },
    {
        "question": "What is the capital city of Zimbabwe?:",
        "options": ["A. Bindura", "B. Chegutu", "C. Chinhoyi", "D. Harare"],
        "answer": "D"
    },
    {
        "question": "Who was the first black president of Zimbabwe?:",
        "options": ["A. Robert", "B. Cannon", "C. Phillimon", "D. Joshua"],
        "answer": "A"
    },
    {
        "question": "What is best used for large scale irrigation?:",
        "options": ["A. Pivot", "B. Drip", "C. Floods", "D. Sprinkler"],
        "answer": "A"
    }
]

# LOGIN SECTION
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful. Proceeding...")
else:
    print("Login failed. Program terminated.")
    exit()

print("Answer the following questions with the appropriate answers: A, B, C, D")

guesses = []
score = 0

# ASK QUESTIONS
for item in quiz:
    print("----------------")
    print(item["question"])

    for opt in item["options"]:
        print(opt)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        print(f"The correct answer is: {item['answer']}")

# RESULTS SECTION
print("__________________________________________________")
print("                     RESULTS                      ")
print("__________________________________________________")

print("Answers: ", end="")
for item in quiz:
    print(item["answer"], end=" ")
print()

print("Guesses: ", end="")
for g in guesses:
    print(g, end=" ")
print()
total_questions = len(quiz)
print(f"\nYou scored {score}/{total_questions}")

percentage = int((score / len(quiz)) * 100)
print(f"Your score in percentage is: {percentage}%")