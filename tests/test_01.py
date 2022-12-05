import unittest
import src.day_01 as day_01


class TestDay_01(unittest.TestCase):
    input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

    def test_part1(self):
        expected = 24000
        result = day_01.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 45000
        result = day_01.part2(self.input)
        self.assertEqual(result, expected)
