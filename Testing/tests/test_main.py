import unittest
from unittest import TestCase

from Testing.main import string_slices, solve, vote

class TestMain(TestCase):
    def test_string_slices(self):
        for i, (param, expected) in enumerate((
                ("%%Приказ об увольнении&#", 'Приказ об увольнении'),
                ("%%Лучший студент на курсе!&#", 'Лучший студент на курсе!'),
                ("%%Hello World!&#", 'Hello World!')
        )):
            with self.subTest(i):
                actual = string_slices(param)
                self.assertEqual(expected, actual)

    def test_vote(self):
        for i, (param, expected) in enumerate((
                ([1,1,1,2,3],(1)),
                ([1,2,2,2,3],(2)),
                ([1,3,3,2,3],(3))
        )):
            with self.subTest(i):
                actual = vote(param)
                self.assertEqual(expected, actual)


    def test_slove(self):
        for i, (param, expected) in enumerate((
                (["нажал кабан на баклажан", "дом как комод"],["нажал кабан на баклажан"]),
                (["рвал дед лавр", "азот калий и лактоза"],["рвал дед лавр", "азот калий и лактоза"]),
                (["а собака боса", "тонет енот", "карман мрак", "пуст суп"],["а собака боса", "тонет енот", "пуст суп"])
        )):
            with self.subTest(i):
                actual = solve(param)
                self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()