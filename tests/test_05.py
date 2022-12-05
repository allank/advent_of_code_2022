import unittest
import src.day_05 as day_05


class TestDay_05(unittest.TestCase):
    input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    def test_part1(self):
        expected = "CMZ"
        result = day_05.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = "MCD"
        result = day_05.part2(self.input)
        self.assertEqual(result, expected)
