import unittest
import src.day_06 as day_06


class TestDay_06(unittest.TestCase):
    input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

    def test_part1(self):
        expected = 7
        result = day_06.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 19
        result = day_06.part2(self.input)
        self.assertEqual(result, expected)
