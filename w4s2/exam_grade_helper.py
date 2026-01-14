def classify_mark(mark: int) -> str:
    if not isinstance(mark, int):
        raise TypeError("Mark must be an integer.")
    if mark < 0 or mark > 100:
        raise ValueError("Mark must be between 0 and 100 inclusive.")
    if mark < 40:
        return "Fail"
    elif mark < 70:
        return "Pass"
    else:
        return "Distinction"


def calculate_summary(marks: list) -> tuple:
    if not isinstance(marks, list):
        raise TypeError("Marks must be a list.")
    if len(marks) == 0:
        return 0, 0, 0, 0

    total = 0
    fail_count = 0
    distinction_count = 0

    for mark in marks:
        if not isinstance(mark, int):
            raise TypeError("All marks must be integers.")
        if mark < 0 or mark > 100:
            raise ValueError("All marks must be between 0 and 100 inclusive.")

        total += mark
        category = classify_mark(mark)
        if category == "Fail":
            fail_count += 1
        elif category == "Distinction":
            distinction_count += 1

    average = total / len(marks)

    return total, average, fail_count, distinction_count
