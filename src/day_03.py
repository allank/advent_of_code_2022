import string


def process_input(input):
    rucksacks = input.splitlines()
    return rucksacks


def make_items(item_string):
    return [i for i in item_string]


def get_priority(letter):
    priorities = [l for l in string.ascii_letters]
    priority = priorities.index(letter) + 1
    return priority


def make_compartments(items):
    num_items = len(items)
    return (items[0 : num_items // 2], items[num_items // 2 :])


def find_common(*elements):
    return list(set(elements[0]).intersection(*elements))


def get_group(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def part1(input):
    rucksacks = process_input(input)
    score = 0
    for rucksack in rucksacks:
        items = make_items(rucksack)
        c1, c2 = make_compartments(items)
        c = find_common(c1, c2)[0]
        score += get_priority(c)
    return score


def part2(input):
    rucksacks = process_input(input)
    score = 0
    for group in get_group(rucksacks, 3):
        group = [make_items(g) for g in group]
        common = find_common(*group)[0]
        score += get_priority(common)
    return score


if __name__ == "__main__":
    # get day number
    day = __file__.split(".")[0].split("_")[-1]
    # get raw input
    with open(f"data/input_{day}.txt", "r") as f:
        input = f.read()
    # TODO: if function returns 0 then this will not print ....
    if result_one := part1(input):
        print(f"Part 1: {result_one}")
    if result_two := part2(input):
        print(f"Part 2: {result_two}")
