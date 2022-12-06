def process_input(input):
    signals = [s for s in input]
    return signals


def get_unique_batch(signals, batch_size):
    for i in range(len(signals)):
        if i > (batch_size - 1):
            batch = signals[i - batch_size : i]
            if len(list(set(batch))) == batch_size:
                return i


def part1(input):
    signals = process_input(input)
    return get_unique_batch(signals, 4)


def part2(input):
    signals = process_input(input)
    return get_unique_batch(signals, 14)


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
