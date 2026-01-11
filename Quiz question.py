# -----------------------------
# QUIZ PROGRAM
# -----------------------------
print("Answer the following questions with the appropriate answers:A,B,C,D ")
questions = (
    "Which one of the following lives under water:",
    "The best gospel artist in Zimbabwe?:",
    "What is the capital city of Zimbabwe?:",
    "Who was the first black president of Zimbabwe?:",
    "What is best used for large scale irrigation?:"
)

options = (
    ("A. DOG", "B. CAT", "C. ZEBRA", "D. FISH"),
    ("A. Charamba", "B. Manyeruke", "C. Zhakata", "D. Mhere"),
    ("A. Bindura", "B. Chegutu", "C. Chinhoyi", "D. Harare"),
    ("A. Robert", "B. Cannon", "C. Phillimon", "D. Joshua"),
    ("A. Pivot", "B. Drip", "C. Floods", "D. Sprinkler")
)

# Correct answers (5 questions → 5 answers)
answers = ("D", "A", "D", "A", "A")

guesses = []
score = 0
question_num = 0

# -----------------------------
# ASK EACH QUESTION
# -----------------------------
for question in questions:
    print("----------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The correct answer is: {answers[question_num]}")

    question_num += 1

# -----------------------------
# RESULTS SECTION
# -----------------------------
print("__________________________________________________")
print("                     RESULTS                      ")
print("__________________________________________________")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

percentage = int((score / len(questions)) * 100)
print(f"Your score in percentage is: {percentage}%")