import unittest
from .Final_Exam import *

class FinalGrader(unittest.TestCase):
    def test_binary_search(self):
        cases = [
            ([1, 2, 3, 4, 5], 1, 0, 4, 0),
            ([2], 2, 0, 0, 0),
            ([1, 3, 13, 55, 66, 77, 88], 77, 0, 6, 5),
            ([1, 3, 13, 55, 66, 77, 88], 33, 0, 6, -1),
            ([], 1, 0, -1, -1),
        ]
        for i, (arg1, arg2, arg3, arg4, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(binary_search(arg1, arg2, arg3, arg4), expected)
    def test_reverse_vowels(self):
        cases = [
            ("hello", "holle"),
            ("world", "world"),
            ("awihatu", "uwahita"),
            ("hello world", "hollo werld"),
            ("", ""),
            ("a", "a"),
        ]
        for i, (arg, expected) in enumerate(cases):
            with self.subTest(test=i):
                self.assertEqual(reverse_vowels(arg), expected)