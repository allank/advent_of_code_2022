import unittest
import src.day_02 as day_02


class TestDay_02(unittest.TestCase):
    input = """A Y
B X
C Z"""

    def test_part1(self):
        expected = 15
        result = day_02.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 12
        result = day_02.part2(self.input)
        self.assertEqual(result, expected)
