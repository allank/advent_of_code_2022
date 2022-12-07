import unittest
import src.day_07 as day_07


class TestDay_07(unittest.TestCase):
    input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    def test_part1(self):
        expected = 95437
        result = day_07.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 24933642
        result = day_07.part2(self.input)
        self.assertEqual(result, expected)
