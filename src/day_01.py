def process_input(input):
    elves = [[int(i) for i in e.splitlines()] for e in input.split("\n\n")]
    return elves


def part1(input):
    elves = process_input(input)
    return sorted([sum(e) for e in elves], reverse=True)[0]


def part2(input):
    elves = process_input(input)
    return sum(sorted([sum(e) for e in elves], reverse=True)[:3])


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
