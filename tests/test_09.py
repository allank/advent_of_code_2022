import unittest
import src.day_09 as day_09


class TestDay_09(unittest.TestCase):
    input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    input2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

    def test_part1(self):
        expected = 13
        result = day_09.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 36
        result = day_09.part2(self.input2)
        self.assertEqual(result, expected)
