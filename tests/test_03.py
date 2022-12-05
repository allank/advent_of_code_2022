import unittest
import src.day_03 as day


class TestDay(unittest.TestCase):
    input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    def test_part1(self):
        expected = 157
        result = day.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 70
        result = day.part2(self.input)
        self.assertEqual(result, expected)
