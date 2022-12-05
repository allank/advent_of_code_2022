import unittest
import src.day_04 as day_04


class TestDay_04(unittest.TestCase):
    input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    def test_part1(self):
        expected = 2
        result = day_04.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 4
        result = day_04.part2(self.input)
        self.assertEqual(result, expected)
