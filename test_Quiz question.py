import unittest
from quiz import calculate_score, correct_answers


class TestQuiz(unittest.TestCase):

    def test_all_answers_correct(self):
        user_answers = ["D", "A", "D", "A", "A"]  # All correct
        score = calculate_score(user_answers, correct_answers)
        self.assertEqual(score, 5)

    def test_single_wrong_answer(self):
        user_answers = ["D", "A", "D", "B", "A"]  # 4 correct
        score = calculate_score(user_answers, correct_answers)
        self.assertEqual(score, 4)

    def test_all_answers_correct(self):
        user_answers = ["D", "A", "D", "A", "A"]  # All correct
        score = calculate_score(user_answers, correct_answers)
        self.assertEqual(score, 5)
    def test_zero_score(self):
        user_answers = ["A", "B", "C", "D", "B"]  # 0 correct
        score = calculate_score(user_answers, correct_answers)
        self.assertEqual(score, 0)

    def test_case_insensitivity(self):
        user_answers = ["d", "a", "d", "a", "a"]  # lowercase but correct
        score = calculate_score(user_answers, correct_answers)
        self.assertEqual(score, 5)

    def test_two_wrong_answers(self):
        user_answers = ["A", "A", "D", "A", "C"]  # 3 correct
        score = calculate_score(user_answers, correct_answers)
        self.assertEqual(score, 3)

    def test_three_wrong_answers(self):
        user_answers = ["A", "B", "D", "C", "A"]  # 2 correct
        score = calculate_score(user_answers, correct_answers)
        self.assertEqual(score, 2)

    def test_wrong_length(self):
        user_answers = ["A", "B"]  # too short
        with self.assertRaises(IndexError):
            calculate_score(user_answers, correct_answers)

    def test_mixed_case_wrong(self):
        user_answers = ["d", "b", "d", "a", "c"]  # 3 correct
        score = calculate_score(user_answers, correct_answers)
        self.assertEqual(score, 3)

    def test_last_answer_wrong(self):
        user_answers = ["D", "A", "D", "A", "C"]  # 4 correct
        score = calculate_score(user_answers, correct_answers)
        self.assertEqual(score, 4)


if __name__ == "__main__":
    unittest.main()