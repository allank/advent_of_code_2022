import math

# needed to get this as a hint for part 2 :(
relief_div = 1


def process_input(input):
    global relief_div
    monkeys_data = input.split("\n\n")

    monkeys = {}
    for monkey_data in monkeys_data:
        monkey_lines = monkey_data.splitlines()
        monkey_id = int(monkey_lines[0].split(":")[0].split(" ")[-1])
        starting_items = monkey_lines[1].split(":")[-1].split(",")
        starting_items = [int(i.strip()) for i in starting_items]
        operation_data = monkey_lines[2].split(" ")
        operation = (operation_data[-2].strip(), operation_data[-1].strip())
        test_divisor = int(monkey_lines[3].split(" ")[-1].strip())
        action_target = {}
        action_target[True] = int(monkey_lines[-2].split(" ")[-1].strip())
        action_target[False] = int(monkey_lines[-1].split(" ")[-1].strip())
        m_data = {}
        m_data["items"] = starting_items
        m_data["op"] = operation
        m_data["test"] = test_divisor
        m_data["targets"] = action_target
        # needed to get this as a hint for part 2 :(
        relief_div = relief_div * test_divisor
        monkeys[monkey_id] = m_data
    return monkeys


def target_monkey(worry, test, target):
    return target[True if worry % test == 0 else False]


def worry_op(start, op):
    if op[1] == "old":
        if op[0] == "+":
            return start + start
        else:
            return start * start
    else:
        if op[0] == "+":
            return start + int(op[1])
        else:
            return start * int(op[1])


def round(monkeys, monkey_count, relief):
    global relief_div
    for monkey, monkey_data in monkeys.items():
        for item in monkey_data["items"]:
            monkey_count[monkey] = monkey_count[monkey] + 1
            worry = worry_op(item, monkey_data["op"])
            # needed to get this as a hint for part 2 :(
            if relief:
                worry = worry % relief_div
            else:
                worry = math.floor(worry / 3)
            monkeys[target_monkey(worry, monkey_data["test"], monkey_data["targets"])][
                "items"
            ].append(worry)
        monkeys[monkey]["items"] = []
    return monkeys, monkey_count


def part1(input):
    monkeys = process_input(input)
    monkey_count = {}
    for k, _ in monkeys.items():
        monkey_count[k] = 0
    for _ in range(20):
        monkeys, monkey_count = round(monkeys, monkey_count, False)
    mb = [v for _, v in monkey_count.items()]
    mb = sorted(mb, reverse=True)
    return mb[0] * mb[1]


def part2(input):
    monkeys = process_input(input)
    monkey_count = {}
    for k, _ in monkeys.items():
        monkey_count[k] = 0
    for _ in range(10000):
        monkeys, monkey_count = round(monkeys, monkey_count, True)
    mb = [v for _, v in monkey_count.items()]
    mb = sorted(mb, reverse=True)
    return mb[0] * mb[1]


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
