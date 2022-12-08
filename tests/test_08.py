import unittest
import src.day_08 as day_08


class TestDay_08(unittest.TestCase):
    input = """30373
25512
65332
33549
35390"""

    def test_part1(self):
        expected = 21
        result = day_08.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 8
        result = day_08.part2(self.input)
        self.assertEqual(result, expected)
