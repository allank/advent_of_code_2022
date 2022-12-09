def process_input(input):
    lines = input.splitlines()
    moves = []
    for line_moves in lines:
        line = line_moves.split(" ")
        moves.append({"move": line[0], "steps": int(line[1])})
    return moves


def resolve_head_move(move, head_pos):
    row = head_pos[0]
    col = head_pos[1]
    if move["move"] == "U":
        row = row + 1
    elif move["move"] == "D":
        row = row - 1
    elif move["move"] == "L":
        col = col - 1
    elif move["move"] == "R":
        col = col + 1
    else:
        # error!
        pass
    return (row, col)


def is_adjacent(head_pos, tail_pos):
    if abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
        return False
    else:
        return True


def resolve_tail_move(head_pos, tail_pos):
    # check if on same position - should never be the case
    if head_pos == tail_pos:
        return head_pos
    if is_adjacent(head_pos, tail_pos):
        return tail_pos
        # adjacent, no need to move
    elif head_pos[0] == tail_pos[0]:
        # in same row, move horizontally
        if head_pos[1] > tail_pos[1]:
            new_pos = (tail_pos[0], tail_pos[1] + 1)
        else:
            new_pos = (tail_pos[0], tail_pos[1] - 1)
        return new_pos
    elif head_pos[1] == tail_pos[1]:
        # in same column, move vertically
        if head_pos[0] > tail_pos[0]:
            new_pos = (tail_pos[0] + 1, tail_pos[1])
        else:
            new_pos = (tail_pos[0] - 1, tail_pos[1])
        return new_pos
    else:
        diff = (head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1])
        if diff[0] > 0 and diff[1] > 0:
            # TR (1, 1)
            delta = (1, 1)
        elif diff[0] < 0 and diff[1] > 0:
            # BR (-1, 1)
            delta = (-1, 1)
        elif diff[0] > 0 and diff[1] < 0:
            # TL (1, -1)
            delta = (1, -1)
        else:  # diff[0] < 0 and diff[1] < 0:
            # BL (-1, -1)
            delta = (-1, -1)
        new_pos = (tail_pos[0] + delta[0], tail_pos[1] + delta[1])
        return new_pos


def part1(input):
    moves = process_input(input)
    head_positions = []
    tail_positions = []
    head_pos = (0, 0)
    tail_pos = (0, 0)
    head_positions.append(head_pos)
    tail_positions.append(tail_pos)
    for move in moves:
        for _ in range(move["steps"]):
            head_pos = resolve_head_move(move, head_pos)
            tail_pos = resolve_tail_move(head_pos, tail_pos)
            head_positions.append(head_pos)
            tail_positions.append(tail_pos)
    return len(list(set(tail_positions)))


def part2(input):
    moves = process_input(input)
    head_positions = []
    tail_positions = []
    head_pos = (0, 0)
    tail_pos = (0, 0)
    head_positions.append(head_pos)
    knot_positions = [tail_pos for _ in range(9)]
    tail_positions.append(knot_positions[-1])
    for move in moves:
        for _ in range(move["steps"]):
            head_pos = resolve_head_move(move, head_pos)
            new_knots = []
            knot_pos = head_pos
            for i in range(len(knot_positions)):
                new_knot = resolve_tail_move(knot_pos, knot_positions[i])
                new_knots.append(new_knot)
                knot_pos = new_knot
            head_positions.append(head_pos)
            tail_positions.append(new_knots[-1])
            knot_positions = new_knots
    return len(list(set(tail_positions)))


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
