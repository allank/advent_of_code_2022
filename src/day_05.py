def process_input(input):
    processed = input.split("\n\n")
    drawing = unpack_drawing(processed[0])
    moves = unpack_moves(processed[1])
    return (drawing, moves)


# TODO: move this into utility library, come up in two days so far
def get_group(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def unpack_drawing(input):
    lines = input.splitlines()
    col_names = lines.pop(-1)
    columns = {}
    for c in get_group(col_names, 4):
        columns[c.strip()] = []
    for line in lines:
        for col, item in enumerate(get_group(line, 4)):
            if item[1].strip():
                columns[str(col + 1)].append(item[1])
    return columns


def unpack_moves(input):
    move_lines = input.splitlines()
    moves = []
    for line in move_lines:
        actions = line.split(" ")
        moves.append({"count": int(actions[1]), "from": actions[3], "to": actions[5]})
    return moves


def process_move(drawing, action):
    for _ in range(action["count"]):
        drawing[action["to"]].insert(0, drawing[action["from"]].pop(0))
    return drawing


def process_move_9000(drawing, action):
    if action["count"] == 1:
        drawing = process_move(drawing, action)
    else:
        drawing[action["to"]] = (
            drawing[action["from"]][0 : action["count"]] + drawing[action["to"]]
        )
        del drawing[action["from"]][0 : action["count"]]
    return drawing


def get_top(drawing):
    top = ""
    for key in drawing.keys():
        top = top + drawing[key][0]
    return top


def part1(input):
    drawing, moves = process_input(input)
    for move in moves:
        drawing = process_move(drawing, move)
    top = get_top(drawing)
    return top


def part2(input):
    drawing, moves = process_input(input)
    for move in moves:
        drawing = process_move_9000(drawing, move)
    top = get_top(drawing)
    return top


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
