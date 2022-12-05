def process_input(input):
    rounds = [(r.split()[0].strip(), r.split()[1].strip()) for r in input.splitlines()]
    return rounds


outcome_score_map = {
    "win": 6,
    "draw": 3,
    "lose": 0,
}

hand_score_map = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}


def play_round(opponent, me):
    if opponent == me:
        return "draw"
    elif (
        (opponent == "rock" and me == "paper")
        or (opponent == "paper" and me == "scissors")
        or (opponent == "scissors" and me == "rock")
    ):
        return "win"
    else:
        return "lose"


def my_hand(opponent, outcome):
    hand_list = ["rock", "paper", "scissors"]
    if outcome == "draw":
        return opponent

    index = hand_list.index(opponent)
    # this feels wrong :)
    if outcome == "win":
        # to win against the opponent, I need the next item in the list
        index = index + 1
        if index >= len(hand_list):
            index = 0
    elif outcome == "lose":
        # to lose against the opponent, I need the previous item in the list
        # don't need to check for negative index, -1 is the last item in a list
        index = index - 1
    return hand_list[index]


def part1(input):
    rounds = process_input(input)
    mapping = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }
    score = 0
    for round in rounds:
        opponent = mapping[round[0]]
        me = mapping[round[1]]
        outcome = play_round(opponent, me)
        score += outcome_score_map[outcome]
        score += hand_score_map[me]
    return score


def part2(input):
    rounds = process_input(input)
    mapping = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }
    score = 0
    for round in rounds:
        opponent = mapping[round[0]]
        me = my_hand(opponent, mapping[round[1]])
        outcome = play_round(opponent, me)
        score += outcome_score_map[outcome]
        score += hand_score_map[me]
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
