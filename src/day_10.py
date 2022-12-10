def process_input(input):
    lines = input.splitlines()
    return lines


def part1(input):
    lines = process_input(input)
    signals = [1]
    for line in lines:
        if line == "noop":
            if len(signals) == 0:
                pass
            else:
                signals.append(signals[-1])
        else:
            jump = int(line.split(" ")[-1])
            for _ in range(1):
                signals.append(signals[-1])
            signals.append(signals[-1] + jump)
    strengths = []
    current = 20
    while current <= 220:
        strengths.append(current * signals[current - 1])
        current = current + 40
    return sum(strengths)


def get_group(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def part2(input):
    lines = process_input(input)
    signals = [1]
    for line in lines:
        if line == "noop":
            if len(signals) == 0:
                pass
            else:
                signals.append(signals[-1])
        else:
            jump = int(line.split(" ")[-1])
            for _ in range(1):
                signals.append(signals[-1])
            signals.append(signals[-1] + jump)
    sprites = ["." for _ in range(240)]
    for i, s in enumerate(signals):
        sprite_positions = [s - 1, s, s + 1]
        pixel_position = i % 40
        if pixel_position in sprite_positions:
            sprites[i] = "#"
    output = []
    for g in get_group(sprites, 40):
        output.append("".join(g))
    display = "\n".join(output)
    print(display)
    return display


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
