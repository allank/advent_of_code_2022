import unittest
import src.day_11 as day_11


class TestDay_11(unittest.TestCase):
    input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

    def test_part1(self):
        expected = 10605
        result = day_11.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 2713310158
        result = day_11.part2(self.input)
        self.assertEqual(result, expected)
