def process_input(input):
    lines = input.splitlines()
    return lines


def part1(input):
    lines = process_input(input)
    return None


def part2(input):
    lines = process_input(input)
    return None


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
