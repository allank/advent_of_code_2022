def process_input(input):
    rucksacks = input.splitlines()
    return rucksacks


def part1(input):
    assignments = process_input(input)
    count = 0
    assignments = input.splitlines()
    for assignment in assignments:
        temp_elves = assignment.split(",")
        elves = []
        for elf in temp_elves:
            elf = (int(elf.split("-")[0]), int(elf.split("-")[1]))
            elves.append(elf)
        if (elves[0][0] <= elves[1][0]) and (elves[0][1] >= elves[1][1]):
            count += 1
        elif (elves[1][0] <= elves[0][0]) and (elves[1][1] >= elves[0][1]):
            count += 1
    return count


def part2(input):
    assignments = process_input(input)
    count = 0
    assignments = input.splitlines()
    for assignment in assignments:
        temp_elves = assignment.split(",")
        elves = []
        for elf in temp_elves:
            elf = (int(elf.split("-")[0]), int(elf.split("-")[1]))
            elves.append(list(range(elf[0], elf[1] + 1)))
        overlap = len(list(set(elves[0]) & set(elves[1])))
        if overlap > 0:
            count += 1
    return count


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
